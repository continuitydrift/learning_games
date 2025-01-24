import random
import time
import datetime

# Initialize variables
current_task = ""
start_time = 0
task_records = []
todo_list = ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5"]

# Function to start tracking time for a new task
def start_task(task_name):
    global current_task, start_time
    current_task = task_name
    start_time = time.time()
    update_display()

# Function to stop tracking the current task and record the time
def stop_task(save_record=False):
    global current_task, start_time, task_records
    if current_task and start_time:
        end_time = time.time()
        elapsed_time = end_time - start_time
        if save_record:
            task_records.append((current_task, datetime.datetime.now(), elapsed_time))
        current_task = ""
        start_time = 0
        update_display()

# Function to show a random quote
def show_quote():
    quotes = ["Quote 1", "Quote 2", "Quote 3", "Quote 4", "Quote 5"]
    random_quote = random.choice(quotes)
    print("Random Quote:", random_quote)

# Function to switch to focus page
def focus_page():
    global current_task
    if current_task == "":
        if input("Set the current task as the top item in the to-do list? (y/n): ").lower() == "y":
            if todo_list:
                current_task = todo_list.pop(0)
    update_display()

# Function to update the display with the current task, timer, and quote
def update_display():
    if current_task:
        print("Current Task:", current_task)
        if start_time:
            elapsed_time = time.time() - start_time
            print("Timer:", int(elapsed_time), "seconds")
        else:
            print("Timer: 0 seconds")
    else:
        print("Current Task:")
        print("Timer: 0 seconds")

# Console-based menu
while True:
    print("\nMenu:")
    print("1) Add Task")
    print("2) Do Something")
    print("3) Show Quote")
    print("4) Save Records")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task_name = input("Enter task name: ")
        start_task(task_name)
    elif choice == "2":
        focus_page()
        while current_task:
            update_display()
            choice = input("\nMenu:\n1) End Turn and Save\n2) End Turn without Saving\n")
            if choice == "1":
                stop_task(save_record=True)
                break
            elif choice == "2":
                stop_task()
                break
    elif choice == "3":
        show_quote()
    elif choice == "4":
        with open("task_records.txt", "a") as file:
            for task, timestamp, time_spent in task_records:
                file.write(f"Task: {task}, Time: {time_spent} seconds, Timestamp: {timestamp}\n")
    else:
        print("Invalid choice. Please select a valid option.")
