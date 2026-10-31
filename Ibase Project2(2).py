import tkinter as tk
from tkinter import ttk
import csv
import statistics

# Employee Data
employees = [
    ["E101", "Amit", "IT", "Present"],
    ["E102", "Riya", "HR", "Absent"],
    ["E103", "Rahul", "IT", "Present"],
    ["E104", "Sneha", "Sales", "Late"],
    ["E105", "Neha", "HR", "Present"],
    ["E106", "Raj", "Sales", "Present"],
    ["E107", "Pooja", "IT", "Absent"]
]

# CSV File Handling
with open("attendance.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Department", "Status"])
    writer.writerows(employees)

# Attendance Analysis
total = len(employees)
present = sum(1 for e in employees if e[3] == "Present")
absent = sum(1 for e in employees if e[3] == "Absent")
late = sum(1 for e in employees if e[3] == "Late")

rate = present / total * 100

# Dashboard Window
root = tk.Tk()
root.title("Employee Attendance Dashboard")
root.geometry("750x550")
root.configure(bg="white")

tk.Label(
    root,
    text="EMPLOYEE ATTENDANCE ANALYTICS",
    font=("Arial", 18, "bold"),
    bg="navy", fg="white", pady=15
).pack(fill="x")

# Summary
summary = tk.Frame(root, bg="white")
summary.pack(pady=20)

values = [
    ("Total", total),
    ("Present", present),
    ("Absent", absent),
    ("Late", late),
    ("Attendance %", round(rate, 2))
]

for i, (name, value) in enumerate(values):
    tk.Label(
        summary,
        text=f"{name}\n{value}",
        font=("Arial", 13, "bold"),
        bg="lightblue",
        width=12,
        height=3
    ).grid(row=0, column=i, padx=5)

# Employee Table
tk.Label(
    root, text="Employee Details",
    font=("Arial", 15, "bold"), bg="white"
).pack(pady=10)

table = ttk.Treeview(
    root,
    columns=("ID", "Name", "Department", "Status"),
    show="headings"
)

for col in ("ID", "Name", "Department", "Status"):
    table.heading(col, text=col)
    table.column(col, width=150)

for employee in employees:
    table.insert("", "end", values=employee)

table.pack(pady=10)

# Department Analysis
tk.Label(
    root,
    text="Department Wise Analysis",
    font=("Arial", 14, "bold"),
    bg="white"
).pack(pady=10)

departments = set(e[2] for e in employees)

for department in sorted(departments):
    count = sum(1 for e in employees if e[2] == department)
    tk.Label(
        root,
        text=f"{department}: {count} Employees",
        bg="white"
    ).pack()

root.mainloop()
