import os
import shutil

def organize_downloads(download_path):
    for filename in os.listdir(download_path):
        file_path = os.path.join(download_path, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            folder = os.path.join(download_path, ext + "_files")
            os.makedirs(folder, exist_ok=True)
            shutil.move(file_path, os.path.join(folder, filename))
    print("Downloads organized successfully!")

if __name__ == "__main__":
    organize_downloads(os.path.expanduser("/Users/rahul/Downloads"))
