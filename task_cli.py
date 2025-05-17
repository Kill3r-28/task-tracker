import sys
import json
import os
from datetime import datetime
from task import Task

TASKS_FILE = "tasks.json"

if __name__ == "__main__":
  if len(sys.argv) < 5:
        print("Usage: python task_cli.py <id> <action> <description> <status>")
        sys.exit(1)
  id = sys.argv[1]
  action = sys.argv[2]
  description = sys.argv[3]
  status = sys.argv[4]
  
  task = Task(id, action, description, datetime.now(), status)
  
  if os.path.exists(TASKS_FILE):
      with open(TASKS_FILE, "r") as f:
          tasks = json.load(f)
  else:
      tasks = []
  
  tasks.append(task.to_dict())
      
  with open(TASKS_FILE, "w") as f:
    json.dump(tasks, f, indent = 2)
  
  
  print("Task created successfully!")
  
  
  # print(f"Id: {task.id}")
  # print(f"Action: {task.action}")
  # print(f"Description: {task.description}")
  # print(f"Date and Time: {task.date_time}")
  # print(f"Status: {task.status}")
  
  