import tkinter as tk
from tkinter import messagebox
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
def stop_task():
    global current_task, start_time, task_records
    if current_task and start_time:
        end_time = time.time()
        elapsed_time = end_time - start_time
        task_records.append((current_task, datetime.datetime.now(), elapsed_time))
        current_task = ""
        start_time = 0
        update_display()

# Function to show a random quote
def show_quote():
    quotes = ["Quote 1", "Quote 2", "Quote 3", "Quote 4", "Quote 5"]
    random_quote = random.choice(quotes)
    messagebox.showinfo("Random Quote", random_quote)

# Function to save task records to a file
def save_records():
    with open("task_records.txt", "a") as file:
        for task, timestamp, time_spent in task_records:
            file.write(f"Task: {task}, Time: {time_spent} seconds, Timestamp: {timestamp}\n")

# Function to switch to focus page
def focus_page():
    global current_task
    if current_task == "":
        if messagebox.askyesno("Set Current Task", "Set the current task as the top item in the to-do list?"):
            if todo_list:
                current_task = todo_list.pop(0)
    update_display()

# Function to update the display with the current task, timer, and quote
def update_display():
    if current_task:
        task_label.config(text="Current Task: " + current_task)
        if start_time:
            elapsed_time = time.time() - start_time
            timer_label.config(text=f"Timer: {int(elapsed_time)} seconds")
        else:
            timer_label.config(text="Timer: 0 seconds")
    else:
        task_label.config(text="Current Task:")
        timer_label.config(text="Timer: 0 seconds")

# Create the main application window
app = tk.Tk()
app.title("Task Tracker")
app.geometry("400x200")
app.configure(bg="darkblue")

# Create GUI elements with white text on a dark blue and grey background
menu_label = tk.Label(app, text="Menu:", bg="darkblue", fg="white")
menu_label.pack()

add_task_button = tk.Button(app, text="1) Add Task", command=lambda: start_task(input("Enter task name: ")), bg="darkblue", fg="white")

add_task_button.pack()

do_something_button = tk.Button(app, text="2) Do Something", command=focus_page, bg="darkblue", fg="white")
do_something_button.pack()

show_quote_button = tk.Button(app, text="Show Quote", command=show_quote, bg="darkblue", fg="white")
show_quote_button.pack()

save_records_button = tk.Button(app, text="Save Records", command=save_records, bg="darkblue", fg="white")
save_records_button.pack()

task_label = tk.Label(app, text="Current Task:", bg="darkblue", fg="white")
task_label.pack()

timer_label = tk.Label(app, text="Timer: 0 seconds", bg="darkblue", fg="white")
timer_label.pack()

# Start the GUI application
app.mainloop()
