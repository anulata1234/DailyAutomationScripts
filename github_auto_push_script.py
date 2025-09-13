import os
import subprocess
from datetime import datetime

def git_push(commit_msg="Auto Commit"):
    try:
        subprocess.run(["git", "add", "."], check=True)
        commit_message = f"{commit_msg} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Code pushed to GitHub successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    git_push("Daily script update")
