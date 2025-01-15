import time
import json

# Function to load tasks from a JSON file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['name']}")

# Function to add a task
def add_task(tasks):
    task_name = input("Enter task name: ")
    task = {"name": task_name, "start_time": time.time(), "end_time": None}
    tasks.append(task)
    print(f"Task '{task_name}' added.")
    save_tasks(tasks)

# Function to remove a task
def remove_task(tasks):
    display_tasks(tasks)
    task_idx = input("Enter the task number to remove (0 to cancel): ")
    if task_idx.isdigit():
        task_idx = int(task_idx)
        if 1 <= task_idx <= len(tasks):
            removed_task = tasks.pop(task_idx - 1)
            print(f"Task '{removed_task['name']}' removed.")
            save_tasks(tasks)
        elif task_idx != 0:
            print("Invalid task number.")
    else:
        print("Invalid input. Please enter a number.")

# Function to start a Pomodoro timer
def start_pomodoro(tasks):
    if tasks:
        task = tasks[-1]
        task["start_time"] = time.time()
        print(f"Pomodoro for '{task['name']}' started.")
        input("Press Enter to stop... ")
        task["end_time"] = time.time()
        save_tasks(tasks)
        print(f"Pomodoro for '{task['name']}' completed!")
    else:
        print("No tasks to start a Pomodoro.")

# Function to display Pomodoro options
def pomodoro_options():
    print("Pomodoro options:")
    print("1. Take a break")
    print("2. Take another turn")
    print("3. Save and quit")
    print("4. Quit without saving")
    print("5. Work on a different task")

# Pomodoro Timer
def pomodoro_timer():
    work_time = 25 * 60  # 25 minutes in seconds
    break_time = 5 * 60  # 5 minutes in seconds

    while True:
        display_tasks(tasks)
        print("\nMain menu:")
        print("1. Start a Pomodoro")
        print("2. Add Task")
        print("3. Remove Task")
        print("0. Quit")

        option = input("Enter an option: ")

        if option == "1":
            start_pomodoro(tasks)
            pomodoro_options()
            pomodoro_option = input("Enter an option (1-5): ")

            if pomodoro_option == "1":
                print("Taking a break...")
                time.sleep(break_time)  # Take a break

            elif pomodoro_option == "2":
                continue  # Start another Pomodoro

            elif pomodoro_option == "3":
                save_tasks(tasks)
                print("Tasks saved. Exiting the Pomodoro app. Have a productive day!")
                break

            elif pomodoro_option == "4":
                print("Exiting the Pomodoro app without saving. Have a productive day!")
                break

            elif pomodoro_option == "5":
                continue  # Continue working on a different task

        elif option == "2":
            add_task(tasks)

        elif option == "3":
            remove_task(tasks)

        elif option == "0":
            save_tasks(tasks)
            print("Exiting the Pomodoro app. Have a productive day!")
            break

if __name__ == "__main__":
    tasks = load_tasks()
    pomodoro_timer()
