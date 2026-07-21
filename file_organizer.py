    import os
import shutil

# ===============================
# File Organizer Using Python
# Author : Sri Vignatha
# Project : USC/UCT Internship
# ===============================

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Python Files": [".py"],
    "Programs": [".exe", ".msi"]
}


def organize_files(folder_path):
    """Organize files into folders based on extension."""

    if not os.path.exists(folder_path):
        print("\nFolder does not exist.")
        return

    moved_files = 0

    for file_name in os.listdir(folder_path):

        source_path = os.path.join(folder_path, file_name)

        if os.path.isdir(source_path):
            continue

        extension = os.path.splitext(file_name)[1].lower()

        destination_folder = "Others"

        for folder, extensions in FILE_TYPES.items():
            if extension in extensions:
                destination_folder = folder
                break

        destination_path = os.path.join(folder_path, destination_folder)

        os.makedirs(destination_path, exist_ok=True)

        shutil.move(
            source_path,
            os.path.join(destination_path, file_name)
        )

        print(f"Moved: {file_name}  →  {destination_folder}")

        moved_files += 1

    print("\n==============================")
    print(" File Organization Completed ")
    print("==============================")
    print(f"Total files moved : {moved_files}")


def main():
    print("===================================")
    print("      FILE ORGANIZER USING PYTHON")
    print("===================================")

    folder = input("\nEnter Folder Path : ").strip()

    organize_files(folder)


if __name__ == "__main__":
    main()
