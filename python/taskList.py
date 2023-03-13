tasks = []

# Function to add a task to the list
def add_task():
	task = input("Enter task name: ")
	tasks.append(task)
	print("Task added.")

# Function to remove a task from the list
def remove_task():
	task = input("Enter task name to remove: ")
	if task in tasks:
    	tasks.remove(task)
    	print("Task removed.")
	else:
    	print("Task not found.")

# Function to print all tasks in the list
def print_tasks():
	if len(tasks) == 0:
    	print("No tasks found.")
	else:
    	print("Tasks:")
    	for task in tasks:
        	print("- " + task)

# Main program loop
while True:
	print("Task List")
	print("1. Add task")
	print("2. Remove task")
	print("3. Print tasks")
	print("4. Quit")
	choice = input("Enter choice: ")
    
	if choice == "1":
    	add_task()
	elif choice == "2":
    	remove_task()
	elif choice == "3":
    	print_tasks()
	elif choice == "4":
    	break
	else:
    	print("Invalid choice.")
