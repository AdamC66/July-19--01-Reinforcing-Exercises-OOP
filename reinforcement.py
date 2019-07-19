# Prerequisites
# Programming fundamentals assignments about data types, variables, conditionals, functions, collections, iteration
# OOP fundamentals
# Exercise 1
# Create a Task class with a description and due_date (both strings).
#  Define an __init__ method, then try creating three instances of this class.

# Exercise 2
# Create a TodoList class with a tasks list (which will contain instances of the Task class). 
# Create an __init__ method and an add_task method that allows you to pass in an instance of your Task class. 
# Try creating a todo list and adding your three tasks to it.

class Task():
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

class To_Do_List():
    def __init__(self):
        self.tasklist=[]

    def add_task(self,description, due_date):
        self.tasklist.append(Task(description,due_date))

    def displaylist(self):
        for task in self.tasklist:
            print(task.description,"-", task.due_date)    

adams_list = To_Do_List()

adams_list.add_task("Get Money", "Tomorrow")
adams_list.add_task("Bro down", "Next week")
adams_list.add_task("Sell out", "Never")

adams_list.displaylist()