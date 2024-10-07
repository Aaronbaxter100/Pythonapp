from tkinter import *
from tkinter import ttk
from tkinter import Toplevel, Text, END, messagebox
import time
import os
import re

window = Tk()
window.geometry('500x500')
window.title('Testing')
window.resizable(width=False, height=False)

user_credentials = {}

def load_user_credentials():
    if os.path.exists('user_credentials.txt'):
        with open('user_credentials.txt', 'r') as f:
            for line in f:
                email, password = line.strip().split(',')
                user_credentials[email] = password

def save_user_credentials():
    with open('user_credentials.txt', 'w') as f:
        for email, password in user_credentials.items():
            f.write(f"{email},{password}\n")

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def apply_theme(theme):
    if theme == "Dark Mode":
        window.config(bg='#36454F')
        main_frame.config(bg='Light grey')
        options_top.config(bg='#36454F')
        Home_button.config(bg='#36454F', fg='white')
        Tasks_button.config(bg='#36454F', fg='white')
        TBC_button.config(bg='#36454F', fg='white')
        Settings_button.config(bg='#36454F', fg='white')
        time_label.config(bg='#36454F', fg='white')
        welcome_label.config(bg='#36454F', fg='white')
    else:
        window.config(bg='White')
        main_frame.config(bg='Light grey')
        options_top.config(bg='Light grey')
        Home_button.config(bg='Light grey', fg='#0097e8')
        Tasks_button.config(bg='Light grey', fg='#0097e8')
        TBC_button.config(bg='Light grey', fg='#0097e8')
        Settings_button.config(bg='Light grey', fg='#0097e8')
        time_label.config(bg='Light grey', fg='black')
        welcome_label.config(bg='Light grey', fg='black')


def login(email, password):
    if email in user_credentials and user_credentials[email] == password:
        messagebox.showinfo("Login Success", "Welcome!")
        login_frame.pack_forget()
        load_main_application()
    else:
        messagebox.showerror("Login Error", "Invalid email or password")

def open_registration_window():
    reg_window = Toplevel(window)
    reg_window.title('Register')
    reg_window.geometry('250x250')
    reg_window.resizable(width=False, height=False)

    register_label = Label(reg_window, text='Register', font='Bold,40')
    register_label.pack(pady=5)

    Label(reg_window, text="Email:").pack(pady=0)
    email_entry = Entry(reg_window)
    email_entry.pack(pady=0)

    Label(reg_window, text="Password:").pack(pady=0)
    password_entry = Entry(reg_window, show='*')
    password_entry.pack(pady=0)

    Button(reg_window, text="Register", command=lambda: register(email_entry.get(), password_entry.get(), reg_window)).pack(pady=10)

def register(email, password, reg_window):
    if not is_valid_email(email):
        messagebox.showerror("Registration Error", "Invalid email format!")
    elif email in user_credentials:
        messagebox.showerror("Registration Error", "Email already exists!")
    elif email == "" or password == "":
        messagebox.showerror("Registration Error", "Email and password cannot be empty!")
    else:
        user_credentials[email] = password
        save_user_credentials()
        messagebox.showinfo("Registration Success", "User registered successfully!")
        reg_window.destroy()

def load_main_application():
    options_top.pack(pady=5)
    options_top.pack_propagate(False)
    options_top.configure(width=500, height=80)

    main_frame.pack(pady=5)
    main_frame.pack_propagate(False)
    main_frame.configure(width=500, height=700)

    indicate(Home_indicate, home_page)
    update_time()

def home_page():
    home_frame = Frame(main_frame)
    home_frame.pack(fill='both', expand=True)

    button_frame = Frame(home_frame, bg='#abb2b9')
    button_frame.pack(side='left', fill='y', padx=0, pady=0)

    test1 = ttk.Button(button_frame, text='Testing One')
    test1.pack(pady=5)

    test2 = ttk.Button(button_frame, text='Testing Two',)
    test2.pack(pady=5)

    lb = Label(home_frame, text='Home Page\n\nPage: 4\n\n \n\n', font=('Bold', 30), bg='Light grey')
    lb.pack()

def task_page():
    # Function to add a new task
    def add_task():
        task = task_entry.get()  # Get the task from entry field
        if task:
            task_listbox.insert(END, task)
            task_states[task] = IntVar()  # Add a checkbox state (unchecked by default)
            task_entry.delete(0, END)  # Clear entry field

    # Function to remove selected task
    def remove_task():
        selected_tasks = task_listbox.curselection()
        for task_index in reversed(selected_tasks):  # Remove from bottom to avoid reindexing issues
            task = task_listbox.get(task_index)
            task_listbox.delete(task_index)
            task_states.pop(task, None)  # Remove state tracking for the task

    # Function to handle checkbox and move task
    def toggle_task():
        for i in range(task_listbox.size()):
            task = task_listbox.get(i)
            if task_states[task].get() == 1:  # Checked
                task_listbox.delete(i)
                task_listbox.insert(END, task)  # Move to the bottom
                task_states[task].set(0)  # Uncheck after moving

    # Main task frame
    task_frame = Frame(main_frame, bg='Light grey')
    task_frame.pack(fill='both', expand=True)

    button_frame = Frame(task_frame, bg='#abb2b9')
    button_frame.pack(side='left', fill='y', padx=0, pady=0)

    lb = Label(task_frame, text='Task page\n\nPage: 2', font=('Bold', 30), bg='Light grey')
    lb.pack()

    # Entry to input new task
    task_entry = Entry(task_frame)
    task_entry.pack(pady=5)

    # Buttons
    new_task = ttk.Button(button_frame, text='Add new task', command=add_task)
    new_task.pack(pady=5)

    remove_task = ttk.Button(button_frame, text='Remove task', command=remove_task)
    remove_task.pack(pady=5)

    # Listbox to display tasks
    task_listbox = Listbox(task_frame, selectmode=MULTIPLE, height=10, width=40)
    task_listbox.pack(pady=10)

    # Checkbox states for each task
    task_states = {}

    # Periodic check for toggled tasks
    task_frame.after(1000, toggle_task)

def tbc_page():
    tbc_frame = Frame(main_frame, bg='Light grey')
    tbc_frame.pack(fill='both', expand=True)

    button_frame = Frame(tbc_frame, bg='#abb2b9')
    button_frame.pack(side='left', fill='y', padx=0, pady=0)

    lb = Label(tbc_frame, text='TBC\n\nPage: 3', font=('Bold', 30), bg='Light grey')
    lb.pack(pady=10)

    button1 = ttk.Button(button_frame, text='Button 1')
    button1.pack(pady=5)

def settings_page():
    settings_frame = Frame(main_frame, bg='Light grey')
    settings_frame.pack(fill='both', expand=True)

    button_frame = Frame(settings_frame, bg='#abb2b9')
    button_frame.pack(side='left', fill='y', padx=0, pady=0)

    button1 = ttk.Button(button_frame, text='Button 1')
    button1.pack(pady=5)

    button2 = ttk.Button(button_frame, text='Button 2')
    button2.pack(pady=5)

    help_button = ttk.Button(button_frame, text='    Help    ', command=help)
    help_button.pack(pady=5)

    theme_options = ['Light Mode', 'Dark Mode']
    theme_dropdown = ttk.Combobox(button_frame, values=theme_options, state='readonly', width=12)
    theme_dropdown.set('Light Mode')
    theme_dropdown.pack(pady=10)

    lb = Label(settings_frame, text='Settings Page\n\nPage: 4\n\n \n\n', font=('Bold', 30), bg='Light grey')
    lb.pack(pady=10)

    def on_theme_change():
        selected_theme = theme_dropdown.get()
        apply_theme(selected_theme)

    theme_dropdown.bind('<<ComboboxSelected>>', on_theme_change)

def hide_indicators():
    Home_indicate.config(bg='Light grey')
    Tasks_indicate.config(bg='Light grey')
    TBC_indicate.config(bg='Light grey')
    Settings_indicate.config(bg='Light grey')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#0097e8')
    delete_pages()
    page()

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    window.after(1000, update_time)

# Indicator bar
options_top = Frame(window)
time_label = Label(options_top, text="Time", font="Arial,18")
time_label.place(x=10, y=0)

Home_button = Button(options_top, text='Home', font=('Arial Bold', 15), bd=0, bg='Light grey', fg='#0097e8', command=lambda: indicate(Home_indicate, home_page))
Home_button.place(x=20, y=40)

Home_indicate = Label(options_top, text='', bg='Light grey')
Home_indicate.place(x=25, y=72, width=55, height=5)

Tasks_button = Button(options_top, text='Tasks', font=('Arial Bold', 15), bd=0, bg='Light grey', fg='#0097e8', command=lambda: indicate(Tasks_indicate, task_page))
Tasks_button.place(x=100, y=40)

Tasks_indicate = Label(options_top, text='', bg='Light grey')
Tasks_indicate.place(x=100, y=72, width=55, height=5)

TBC_button = Button(options_top, text='TBC', font=('Arial Bold', 15), bd=0, bg='Light grey', fg='#0097e8', command=lambda: indicate(TBC_indicate, tbc_page))
TBC_button.place(x=180, y=40)

TBC_indicate = Label(options_top, text='', bg='Light grey')
TBC_indicate.place(x=180, y=72, width=55, height=5)

Settings_button = Button(options_top, text='Settings', font=('Arial Bold', 15), bd=0, bg='Light grey', fg='#0097e8', command=lambda: indicate(Settings_indicate, settings_page))
Settings_button.place(x=250, y=40)

Settings_indicate = Label(options_top, text='', bg='Light grey')
Settings_indicate.place(x=250, y=72, width=55, height=5)

# Main content area
main_frame = Frame(window)

# Login frame
login_frame = Frame(window)
login_frame.pack(pady=10)

login_label = Label(login_frame, text='Login', font='Bold,40')
login_label.pack(pady=5)

Label(login_frame, text="Email:").pack(pady=0)
email_entry = Entry(login_frame)
email_entry.pack(pady=0)

Label(login_frame, text="Password:").pack(pady=0)
password_entry = Entry(login_frame, show='*')
password_entry.pack(pady=0)

Button(login_frame, text="Login", command=lambda: login(email_entry.get(), password_entry.get())).pack(pady=10)

Button(login_frame, text="Register", command=open_registration_window).pack()

# Load user credentials on app start
load_user_credentials()

window.mainloop()
