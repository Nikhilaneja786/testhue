import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import csv

# Initialize an empty list to store attendance data
attendance_data = []

# Function to mark a student as present
def mark_present():
    student_name = name_entry.get()
    if student_name:
        # Check for duplicate entries
        for entry in attendance_data:
            if entry[0] == student_name:
                messagebox.showinfo("Duplicate Entry", f"{student_name} is already marked.")
                return

        current_time = datetime.datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        attendance_data.append((student_name, "Present", timestamp))
        status_label.config(text=f"{student_name} is Present")
        name_entry.delete(0, tk.END)

# Function to mark a student as absent
def mark_absent():
    student_name = name_entry.get()
    if student_name:
        for entry in attendance_data:
            if entry[0] == student_name:
                messagebox.showinfo("Duplicate Entry", f"{student_name} is already marked.")
                return

        current_time = datetime.datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        attendance_data.append((student_name, "Absent", timestamp))
        status_label.config(text=f"{student_name} is Absent")
        name_entry.delete(0, tk.END)

# Function to display attendance data
def show_attendance():
    attendance_window = tk.Toplevel(root)
    attendance_window.title("Attendance Data")
    
    tree = ttk.Treeview(attendance_window, columns=("Name", "Status", "Timestamp"))
    tree.heading("#1", text="Name")
    tree.heading("#2", text="Status")
    tree.heading("#3", text="Timestamp")
    
    for entry in attendance_data:
        tree.insert("", "end", values=entry)
    
    tree.pack()

# Function to save attendance data to a CSV file
def save_attendance():
    with open("attendance.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Status", "Timestamp"])
        writer.writerows(attendance_data)

# Function to load attendance data from a CSV file
def load_attendance():
    try:
        with open("attendance.csv", mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            attendance_data.extend([row for row in reader])
    except FileNotFoundError:
        messagebox.showinfo("File Not Found", "No attendance data file found.")

# Create the main tkinter window
root = tk.Tk()
root.title("Attendance System")
root.geometry('1910x1020')

# Create and pack widgets
name_label = tk.Label(root, text="Student Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

present_button = tk.Button(root, text="Mark Present", command=mark_present)
present_button.grid(row=1, column=0, padx=5, pady=5)

absent_button = tk.Button(root, text="Mark Absent", command=mark_absent)
absent_button.grid(row=1, column=1, padx=5, pady=5)

status_label = tk.Label(root, text="")
status_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

show_button = tk.Button(root, text="Show Attendance", command=show_attendance)
show_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

save_button = tk.Button(root, text="Save Attendance", command=save_attendance)
save_button.grid(row=4, column=0, padx=5, pady=5)

load_button = tk.Button(root, text="Load Attendance", command=load_attendance)
load_button.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()