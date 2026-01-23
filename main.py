'''
    This is where the main loop is going to be.

    List of what is going to be structured here:

    1. Initialize database
    2. Show menu
    3. Get user choices
    4. do the action
    5. Repeat until exit

'''

from database import (
    Initialize_database,
    list_tasks,
    Add_task,
    Update_task,
    Delete_task
)

def show_menu():
    print("\n===== To-Do List =====")
    print("1. View tasks")
    print("2. Add Task")
    print("3. Mark task complete")
    print("4. Delete task")
    print("5. Exit")

def main():
    Initialize_database()

    while True:
        show_menu()
        choice = input("\nEnter choice (1-5): ")

        if choice == "1":
            tasks = list_tasks()
            if tasks:
                print("\nThis is list:")
                for task in tasks:
                    print(f'{task[0]}.{task[1]} - Status: {task[2]}')
            else:
                print('\nThere are no tasks.')
        elif choice == '2':
            Add_task(input('\nWhat is the task you would like to add?' ))
            print('\nTask Successfully Added.')
        elif choice == '3':
            Update_task(input("\nWhich Task would you like to change to complete? if you dont remmeber exit and ask for list and then choose:"))
            print('\nStatus Changed to complete.')
        elif choice == '4':
            Delete_task(input('which task would you like to delete. if you dont remember exit and ask for list. then choose:'))
            print("we have successfully deleted the task.")
        elif choice == '5':
            print('goodbye!')
            break
        else:
            print('Invalid choice. Try again.')

if __name__ == '__main__':
    main()