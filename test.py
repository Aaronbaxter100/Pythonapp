import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import Toplevel, Text, END, messagebox
import time
import os
import speedtest

from test import show_login_window

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
        login_frame.pack_forget()  # Hide login frame
        load_main_application()  # Load main application on successful login
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
        save_user_credentials()  # Save to file when registering
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

def task_page():
    task_frame = Frame(main_frame, bg='Light grey')

    button_frame = Frame(task_frame, bg='#abb2b9')
    button_frame.pack(side='left', fill='y', padx=0, pady=0)

    lb = Label(task_frame, text='Task page\n\nPage: 2', font=('Bold', 30), bg='Light grey')
    lb.pack()
    task_frame.pack()

def tbc_page():
    tbc_frame = Frame(main_frame, bg='Light grey')
    tbc_frame.pack(fill='both', expand=True)

    button_frame = Frame(tbc_frame, bg='#abb2b9')
    button_frame.pack(side='left', fill='y', padx=0, pady=0)

    lb = Label(tbc_frame, text='TBC\n\nPage: 3', font=('Bold', 30), bg='Light grey')
    lb.pack(pady=10)

def settings_page():
    settings_frame = Frame(main_frame, bg='Light grey')
    settings_frame.pack(fill='both', expand=True)

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
    lb.config(bg='Blue')
    delete_pages()
    page()

def update_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time)
    window.after(1000, update_time)

# Toggle password visibility function
def toggle_password():
    if show_password_var.get():
        password_entry.config(show='')  # Show the password
    else:
        password_entry.config(show='*')  # Hide the password (use *)

# Frame
login_frame = Frame(window)
login_frame.pack(fill='both', expand=True)

login_spacer = Label(login_frame, text= '       ',font = 'Bold,40')
login_spacer.pack(pady=40)

login_label = Label(login_frame, text= 'Login',font = 'Bold,40')
login_label.pack(pady=5)

Label(login_frame, text="Username:").pack(pady=0)
username_entry = Entry(login_frame)
username_entry.pack(pady=0)

Label(login_frame, text="Password:").pack(pady=0)
password_entry = Entry(login_frame, show='*')
password_entry.pack(pady=0)

# Show Password checkbox
show_password_var = IntVar()  # Integer variable to track checkbox state
show_password_checkbox = Checkbutton(login_frame, text="Show Password", variable=show_password_var, command=toggle_password)
show_password_checkbox.pack(pady=5)

ttk.Button(login_frame, text="Login", command=lambda: login(username_entry.get(), password_entry.get())).pack(pady=10)
ttk.Button(login_frame, text="Register", command=open_registration_window).pack(pady=10)

options_top = Frame(window, bg='Light grey')
main_frame = Frame(window, bg='Light grey')

welcome_label = Label(options_top, text="Welcome", font=('Bold', 12), fg='Black', bg='Light grey')
welcome_label.place(x=200, y=0)

time_label = Label(options_top, text="", font=('Bold', 7), fg='Black', bg='Light grey')
time_label.place(x=420, y=0)

Home_button = Button(options_top, text='Home', font=('Arial', 13), bd=0, fg='#0097e8', bg='Light grey',
                     activeforeground='Light grey', command=lambda: indicate(Home_indicate, home_page))
Home_button.place(x=0, y=20, width=125)

Home_indicate = Label(options_top, text="", bg='#abb2b9')
Home_indicate.place(x=45, y=50, width=35, height=5)

Tasks_button = Button(options_top, text='Tasks', font=('Arial', 13), bd=0, fg='#0097e8', bg='Light grey',
                      activeforeground='Light grey', command=lambda: indicate(Tasks_indicate, task_page))
Tasks_button.place(x=125, y=20, width=125)

Tasks_indicate = Label(options_top, text="", bg='Light grey')
Tasks_indicate.place(x=170, y=50, width=35, height=5)

load_user_credentials()
update_time()
window.mainloop()
