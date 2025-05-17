import sys
from datetime import datetime
from task import Task


if __name__ == "__main__":
  if len(sys.argv) < 5:
        print("Usage: python task_cli.py <id> <action> <description> <status>")
        sys.exit(1)
  id = sys.argv[1]
  action = sys.argv[2]
  description = sys.argv[3]
  status = sys.argv[4]
  
  task = Task(id, action, description, datetime.now(), status)
  print("Task created successfully!")
  
  print(f"Id: {task.id}")
  print(f"Action: {task.action}")
  print(f"Description: {task.description}")
  print(f"Date and Time: {task.date_time}")
  print(f"Status: {task.status}")