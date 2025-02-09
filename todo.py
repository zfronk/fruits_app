# Called when object is intialized - init
class ToDoListManager:
    def __init__(self):
        self.tasks = [] # Empty list to store tasks

    # Display main menu
    def display_main_menu(self):

        print()
        print("Welcome to the To-Do List Manager!")

        print()
        print("Main Menu")
        print("---------")
        print("1. Add a task.")
        print("2. Remove a task.")
        print("3. Display all tasks.")
        print("4. Update task.")
        print("5. Exit application.")

    # Choose an option
    def choose_option(self):
        option = int(input("# Choose an option from the main menu: "))
        return option 
    
    # Add a task
    def add_task(self):

        try:
            print()
            print("Adding a task...")
            task = str(input("Enter task to be added: ").capitalize())

            if task == "":
                print("Task cannot be empty!")
                return
        
            else:

            # New task dictonary
                new_task = {
                "task":task,
                "completed": False
            }

            
            self.tasks.append(new_task)
        
            print()
            print("Task added successfully!")


        except ValueError:
            print("Error adding task!")

    # Remove a task
    def remove_task(self):
        try:
            self.display_tasks()

            while True:
                print()
                task_to_delete = int(input("Enter task to be deleted: "))

                if not task_to_delete:
                    print()
                    print("Task cannot be empty!")  
                
                else:
                    task_index = task_to_delete - 1

                    if task_index < 0 or task_index >= len(self.tasks):
                        print()
                        print("Invalid task number. Please try again.")
                        continue

                    else:
                        del self.tasks[task_index]
                        print()
                        print("Task deleted successfully!")
                        break


        except ValueError:
            print("Error occured while removing task!")  

    # Update a task
    def update_task(self):
        try:
            self.display_tasks()
            while True:
                print()
                task_to_update = int(input("Enter task to be updated: "))
                task_index = task_to_update - 1 # Index of task to be updated as per array

                if not task_to_update:
                    print("Task cannot be empty!")

                elif task_index < 0 or task_to_update > len(self.tasks):
                    print("Invalid task number. Please try again.")
                    continue 
                else:
                    
                    old_task = self.tasks[task_index]
                    print()
                    print(f"Task to be updated: {old_task["task"]} | Completed: {old_task["completed"]}")

                    print()
                    update_query = str(input("Are you updating the task, (completion status)? (y/n): "))

                    update_query = update_query.lower()

                    print()
                    if update_query == "y":
                        print("Updating completion status...")
                        completion_status = str(input("Enter completion status (True/False): "))

                        completion_status = completion_status.capitalize()
                        task_to_modify = self.tasks[task_index]
                        task_to_modify["completed"] = completion_status

                        print()
                        print("Task completion status updated successfully!")
                        break
                    
                    elif update_query == "n":
                        print("Guess you're updating it to a new task right?")
                        new_task = str(input("Enter new updated task: ").capitalize())

                        if new_task == "":
                            print("Task cannot be empty!")
                            continue

                        else:
                            task_to_modify = self.tasks[task_index]
                            task_to_modify["task"] = new_task

                            print()
                            print("Task updated successfully!")
                            break

                    

        except ValueError:
            print("Error updating task!")
                     
             
    # Display tasks
    def display_tasks(self):
        try:
            if self.tasks == []:
                print()
                print("No tasks available!")

            else:
                print()
                print("Tasks")
                print("-----")
                for index, task in enumerate(self.tasks, start=1):
                    print(f"{index}. {task['task']} | Completed: {task['completed']}")

        except ValueError:
            print("Error displaying tasks!")
        


    # Run the application
    def run(self):
        try:
            self.display_main_menu()

            while True:
            
                print()
                option = self.choose_option()
                if option == 1:
                    self.add_task()
                elif option == 2:
                    self.remove_task()
                elif option == 3:
                    self.display_tasks()
                elif option == 4:
                    self.update_task()
                elif option == 5:
                    print()
                    print("Exiting application...")
                    break
                else:
                    print("Invalid option. Please try again.")

        except ValueError:
            print("Error running application!")



        

# Run the application
if __name__ == "__main__":
    app = ToDoListManager()
    app.run()
    