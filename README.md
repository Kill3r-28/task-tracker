# Define what a task looks like
- every task will have a `unique id`, `add/update/done` `description`, `date and time` created and `status`
- so before creating a task, unique id must be checked for availability and status must be set to "incomplete"


# Logic to implement command line arguments
- command line code to create/update/del must look like this
  - task id add/update "submit week 1 and 2 assignments of dbms course"
  - task id done
  - task list
  - task list -1

# Reqs
- after 30 days tasks must be deleted (so there's only a month's time to finish those tasks or forget them)