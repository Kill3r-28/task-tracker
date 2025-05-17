from datetime import datetime

class Task:
  def __init__(self, id, action, description, date_time, status="incomplete"):
    self.id = id
    self.action = action
    self.description = description
    self.date_time = datetime.now()
    self.status = status
    
    
  def to_dict(self):
    return {
      "id": self.id,
      "action": self.action,
      "description": self.description,
      "date_time": self.date_time.isoformat(),
      "status": self.status
    }