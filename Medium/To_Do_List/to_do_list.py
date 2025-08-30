# To-Do List Application (Console Based)

# Empty list to store tasks
to_do_list = []

# Menu options
print("---- To-Do List ----")
print("1 -> View tasks")
print("2 -> Add a task")
print("3 -> Delete a task")
print("4 -> Exit")

# Infinite loop until user exits
while True:

    choice = input("\nChoose an option (1 to 4): ")

    # View tasks
    if choice == '1':
        if to_do_list:
            print("The tasks present in the list:")
            for i, task in enumerate(to_do_list):
                print(f"\t{i+1}. {task}")
        else:
            print("No tasks added yet.")

    # Add a task
    elif choice == '2':
        task = input("Enter the task to be added: ")
        to_do_list.append(task)
        print("The task has been added to the list.")

    # Delete a task
    elif choice == '3':
        idx = input("Enter the task number to be deleted: ")
        try:
            idx = int(idx)
        except ValueError:
            print("Please enter a valid number.")
        else:
            if 0 < idx <= len(to_do_list):
                deleted = to_do_list.pop(idx-1)
                print(f"The task '{deleted}' has been removed from the list.")
            else:
                print("Enter a valid task number.")

    # Exit
    elif choice == '4':
        print("---- Thank You for using To-Do List! ----")
        break

    # Invalid choice
    else:
        print("Enter a valid option only (1 to 4).")

print("---- Program Ended ----")
