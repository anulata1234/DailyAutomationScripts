import json
from datetime import datetime

def add_task(task):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"tasks_{today}.json"

    try:
        with open(filename, "r") as f:
            tasks = json.load(f)

    except FileNotFoundError:
        tasks = []

    tasks.append({"task": task, "time": datetime.now().strftime("%H:%M:%S")})

    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)

    print("Task added successfully!")

if __name__ == "__main__":

    add_task("Complete Python GitHub Automation Project")
