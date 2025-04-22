# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.

# test that an emoty list is produced
# mark task as complete
# remove themm from the list
class Task:
    def __init__(self):
        self.todo_list = []
        self.completed_tasks = []

    def add(self, task):
        self.todo_list.append(task)

    def completed(self, task):
        if task in self.todo_list:
            self.completed_tasks.append(task)

    def remove(self, task):
        if task in self.completed_tasks:
            self.todo_list.remove(task)
        return self.todo_list