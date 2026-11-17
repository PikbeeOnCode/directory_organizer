# 📁 Directory Organizer

A Python-based file organization tool that automatically sorts files into categorized folders based on their file extensions.

Built using Python's `pathlib` and `shutil` modules, this project demonstrates practical file handling, directory management, conditional logic, exception handling, and automation.

##  Features

- **Automatic File Categorization:** Organizes files based on their extensions.
- **Multiple File Categories:** Supports images, documents, audio, videos, archives, and code files.
- **Duplicate Filename Handling:** Prevents files from being overwritten when duplicate filenames exist.
- **Error Handling:** Handles file operation errors gracefully.
- **Extension Normalization:** Handles file extensions consistently, regardless of capitalization.
- **Directory Skipping:** Skips directories instead of treating them as regular files.
- **File Organization Report:** Generates a report containing information about the organization process.

## 📂 Supported File Categories

| Category | Supported Extensions |
|---|---|
| Images | jpg, jpeg, png, gif, webp |
| Documents | pdf, txt, docx, doc |
| Audio | mp3, wav, flac |
| Videos | mp4, mkv, mov |
| Archives | zip, rar, 7z |
| Code | py, js, html, css, json |
| Others | Other files with extensions |

Files without extensions are skipped.

## 🛠️ Technologies Used

- **Python** – Core programming language.
- **pathlib** – File and directory path management.
- **shutil** – Moving files between directories.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/directory_organizer.git
```

### 2. Navigate to the Project Directory

```bash
cd directory_organizer
```

### 3. Configure the Target Directory

Update the target directory in `main.py` to specify which directory you want to organize.

### 4. Run the Project

```bash
python main.py
```

The program will scan the target directory and move files into their respective category folders.

## 📋 Project Scope

This is a first-version file organization tool.

**Included:**
- Extension-based file categorization.
- File movement and folder creation.
- Duplicate filename handling.
- Exception handling.
- Organization report generation.

**Not included in this version:**
- Recursive directory scanning.
- Automatic Downloads folder monitoring.
- Background file organization.

## 🎯 Learning Objectives

This project was built to practice:

- Working with files and directories.
- Using Python's built-in modules.
- Understanding dictionaries and conditional statements.
- Implementing loops and helper functions.
- Handling exceptions.
- Automating repetitive file management tasks.

## 👨‍💻 Author

Developed as part of my Python learning and practical automation projects.
