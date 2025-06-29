import tkinter as tk

# Create main window
win = tk.Tk()
win.title("Task Manager")
win.geometry("600x800")
win.config(bg="#C37F7F")

# Title label
name_label = tk.Label(win, text="Task Manager", font=("Poppins", 22, "bold"), bg="#C37F7F", fg="#E7E2E2")
name_label.place(x=150, y=50, width=300)

# Scrollable Frame Setup
main_canvas = tk.Canvas(win, bg="#FFFFFF", highlightthickness=0)
scrollbar = tk.Scrollbar(win, orient="vertical", command=main_canvas.yview)
scrollable_frame = tk.Frame(main_canvas, bg="#FFFFFF")

scrollable_frame.bind(
    "<Configure>",
    lambda e: main_canvas.configure(
        scrollregion=main_canvas.bbox("all")
    )
)

main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
main_canvas.configure(yscrollcommand=scrollbar.set)

main_canvas.place(x=25, y=150, width=550, height=600)
scrollbar.place(x=565, y=150, height=600)

# Headers
tk.Label(scrollable_frame, text="✔", font=("Helvetica", 14), bg="#FFFFFF").grid(row=0, column=0, padx=5)
tk.Label(scrollable_frame, text="Time", font=("Helvetica", 14), bg="#FFFFFF").grid(row=0, column=1, padx=10)
tk.Label(scrollable_frame, text="Task", font=("Helvetica", 14), bg="#FFFFFF").grid(row=0, column=2, padx=10)
tk.Label(scrollable_frame, text="Actions", font=("Helvetica", 14), bg="#FFFFFF").grid(row=0, column=3, padx=10)

# Store rows
rows = []

# Add a new task row
def add_task_row():
    row_index = len(rows) + 1
    time_var = tk.StringVar()
    task_var = tk.StringVar()
    done_var = tk.IntVar()

    # Widgets
    check_btn = tk.Checkbutton(scrollable_frame, variable=done_var, bg="#FFFFFF",
                                command=lambda: toggle_done(task_entry, done_var))
    time_entry = tk.Entry(scrollable_frame, textvariable=time_var, font=("Helvetica", 12),
                          width=10, bg="#B91010", fg="white")
    task_entry = tk.Entry(scrollable_frame, textvariable=task_var, font=("Helvetica", 12),
                           width=30, bg="#B91010", fg="white")

    edit_btn = tk.Button(scrollable_frame, text="Edit", font=("Helvetica", 10),
                         command=lambda: edit_task(task_entry, time_entry))
    delete_btn = tk.Button(scrollable_frame, text="❌", font=("Helvetica", 10),
                           command=lambda: delete_task(row_widgets))

    # Layout
    check_btn.grid(row=row_index, column=0, padx=5, pady=5)
    time_entry.grid(row=row_index, column=1, padx=10, pady=5)
    task_entry.grid(row=row_index, column=2, padx=10, pady=5)
    edit_btn.grid(row=row_index, column=3, sticky='w')
    delete_btn.grid(row=row_index, column=3, sticky='e')

    def on_enter(event):
        time_entry.config(state='disabled')
        task_entry.config(state='disabled')
        add_task_row()

    task_entry.bind("<Return>", on_enter)

    row_widgets = (check_btn, time_entry, task_entry, edit_btn, delete_btn)
    rows.append(row_widgets)

# Checkbox action
def toggle_done(task_entry, done_var):
    if done_var.get() == 1:
        task_entry.config(fg="gray")
    else:
        task_entry.config(fg="white")

# Delete task row
def delete_task(row_widgets):
    for widget in row_widgets:
        widget.destroy()
    rows.remove(row_widgets)

# Edit both task and time
def edit_task(task_entry, time_entry):
    task_entry.config(state='normal')
    time_entry.config(state='normal')
    task_entry.focus_set()

# Add initial row
add_task_row()

# Run app
win.mainloop()
