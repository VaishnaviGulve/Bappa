
import os
def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename,'r') as file:
            tasks = file.read().splitlines()
    else:
        tasks = []
    return tasks

def save_tasks(filename, tasks):
    with open(filename,'w')as file:
        for task in tasks:
            file.write(task + '\n')

def display_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def remove_task(tasks):
    display_tasks(tasks)
    if tasks:
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("Task removed.")
        else:
            print("Invalid task number.")

def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)

    while True:
        print("\nTodo List:")
        display_tasks(tasks)
        print("\nOptions:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Exist")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            save_tasks(filename, tasks)
            print("Tasks saved. Existing.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
