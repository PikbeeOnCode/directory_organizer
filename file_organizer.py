from pathlib import Path
import shutil

file_categories = {
    "Images": ["jpg", "jpeg", "png", "gif", "webp"],
    "Documents": ["pdf", "txt", "docx", "doc"],
    "Audio": ["mp3", "wav", "flac"],
    "Videos": ["mp4", "mkv", "mov"],
    "Archives": ["zip", "rar", "7z"],
    "Code": ["py", "js", "html", "css", "json"]
}



BASE_DIR = Path(__file__).resolve().parents[3]

targeted_scan_directory = BASE_DIR/"testing"/"directory_test"

report_path = BASE_DIR/"day_eleven"/"pratice"/"automation_projects"/"file_organizer_report.txt"

total_file_scanned = 0
succesfully_moved_file = 0 
failed_files = 0
files_skipped = 0 
unsupported_file = 0


#  scanning target directory 

for file in targeted_scan_directory.iterdir():
    if file.is_file():
        try:
            total_file_scanned+=1
            file_extension = file.suffix.lstrip(".").lower()
            category = "others"
            for folder,extensions  in file_categories.items():
                if file_extension in extensions:
                    category = folder
                    break

            if category == "others":
                unsupported_file +=1
               
            destination_dir = targeted_scan_directory/category
            destination_dir.mkdir(parents=True,exist_ok=True)
            destination_path = destination_dir/file.name
            counter = 1
            while destination_path.exists():
                file_name = f"{file.stem}({counter}){file.suffix}"
                destination_path = destination_dir/file_name
                counter +=1

            shutil.move(str(file),str(destination_path))
            succesfully_moved_file+=1
        except PermissionError:
            print(f"Permission denied: {file.name}")
            failed_files +=1
        except FileNotFoundError:
            print(f"File disappeared: {file.name}")
            failed_files +=1
        except OSError as error:
            print(f"Filesystem error: {file.name} - {error}")
            failed_files +=1
    else:
        files_skipped+=1          

# scanned and file move report   

report = f"""
========================================
          FILE ORGANIZER REPORT
========================================

Directory scanned : {targeted_scan_directory}

--------------- SUMMARY ---------------

Total files scanned       : {total_file_scanned}
Successfully moved        : {succesfully_moved_file}
Unsupported files moved   : {unsupported_file}
Failed files              : {failed_files}
Directories skipped      : {files_skipped}

========================================
             END OF REPORT
========================================
"""

try:
    report_path.touch(exist_ok=True)

    with open(report_path,"w") as file:
        file.write(report)
        print("Report generated successfully!")
except OSError as error:
    print(f"Unable to generate report: {error}")
