from tkinter import *
from tkinter import ttk
import time
from tkinter import Toplevel, Text, END

window = Tk()
window.geometry('500x500')
window.title('Testing')
window.resizable(width=False, height=False)

def apply_theme(theme):
    if theme == "Dark Mode":
        window.config(bg='#36454F')
        main_frame.config(bg='#36454F')
        options_top.config(bg='#36454F')
        Home_button.config(bg='#36454F', fg='white')
        Tasks_button.config(bg='#36454F', fg='white')
        TBC_button.config(bg='#36454F', fg='white')
        Settings_button.config(bg='#36454F', fg='white')
        time_label.config(bg='#36454F', fg='white')
    else:
        window.config(bg='light grey')
        main_frame.config(bg='pink')
        options_top.config(bg='light grey')
        Home_button.config(bg='light grey', fg='#0097e8')
        Tasks_button.config(bg='light grey', fg='#0097e8')
        TBC_button.config(bg='light grey', fg='#0097e8')
        Settings_button.config(bg='light grey', fg='#0097e8')
        time_label.config(bg='light grey', fg='black')

def home_page():
    home_frame = Frame(main_frame)
    home_frame.pack(pady=20, anchor='w')

    test1 = Button(home_frame, text = 'Testing One', font = 'Bold,40')
    test1.grid(row = 2, column = 0, sticky='w')

    test2 = Button(home_frame, text='Testing Two', font = 'Bold,40',)
    test2.grid(row=3, column=0, sticky='w')

    home_frame.pack(pady=20)

def task_page():
    task_frame = Frame(main_frame, bg = 'Light grey')

    lb = Label(task_frame, text='Task page\n\nPage: 2', font=('Bold', 30), bg = 'Light grey')
    lb.pack()

    task_frame.pack()

def tbc_page():
    tbc_frame = Frame(main_frame, bg = 'Light grey')

    lb = Label(tbc_frame, text='TBC\n\nPage: 3', font=('Bold', 30),bg = 'Light grey')
    lb.pack()

    tbc_frame.pack(pady=20)

def settings_page():

    settings_frame = Frame(main_frame, bg = 'Light grey')
    settings_frame.pack(fill='both', expand=True)

    button_frame = Frame(settings_frame, bg = 'grey')
    button_frame.pack(side='left', fill='y', padx=0, pady=0)

    button1 = Button(button_frame, text='Button 1', font = ('bold', 10))
    button1.pack(pady=5)

    button2 = Button(button_frame, text='Button 2', font = ('bold', 10))
    button2.pack(pady=5)

    help_button = Button(button_frame, text='    Help    ', font = ('bold', 10), command=help)
    help_button.pack(pady=5)

    theme_options = ['Light Mode', 'Dark Mode']
    theme_dropdown = ttk.Combobox(button_frame, values=theme_options, state='readonly')
    theme_dropdown.set('Light Mode')
    theme_dropdown.pack(pady=10)

    lb = Label(settings_frame, text='Settings Page\n\nPage: 4\n\n \n\n', font=('Bold', 30), bg='Light grey')
    lb.pack(pady=10)

    def on_theme_change(event):
        selected_theme = theme_dropdown.get()
        apply_theme(selected_theme)

    theme_dropdown.bind('<<ComboboxSelected>>', on_theme_change)

    settings_frame.pack(pady=20)

def hide_indicators():
    Home_indicate.config(bg='light grey')
    Tasks_indicate.config(bg='light grey')
    TBC_indicate.config(bg='light grey')
    Settings_indicate.config(bg='light grey')

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

def help():
    help_window = Toplevel(window)
    help_window.title('Help')
    help_window.geometry('400x400')
    help_window.resizable(width=False, height=False)

    help_label = Label(help_window, text="This is the Help section.", font=('Arial', 15))
    help_label.pack(pady=5)

    info_label = Label(help_window, text="Please tell us how we can help? ", font=('Arial', 15))
    info_label.pack(pady=5)

    message_text = Text(help_window, font=('Arial', 12), height=5, width=40)
    message_text.pack(pady=10)

    def limit_chars(event=None):
        current_text = message_text.get("1.0", END)
        if len(current_text) > 200:
            message_text.delete("1.0", END)
            message_text.insert("1.0", current_text[:200])

    message_text.bind("<KeyRelease>", limit_chars)

    def submit_message():
        message = message_text.get("1.0", END).strip()
        if len(message) > 200:
            print("Error: Message exceeds 20 characters!")
        else:
            print(f"Submitted message: {message}")
            message_text.delete("1.0", END)

    submit_button = Button(help_window, text="Submit", font=('Arial', 12), command=submit_message)
    submit_button.pack(pady=10)

# Frames
options_top = Frame(window, bg='light grey')
options_top.pack(pady=5)
options_top.pack_propagate(False)
options_top.configure(width=500, height=55)

main_frame = Frame(window, bg='Light grey')
main_frame.pack(pady=5)
main_frame.pack_propagate(False)
main_frame.configure(width=500, height=700)

# Labels
welcome_label = Label(options_top, text="Welcome", font=('Bold', 12), fg = 'Black',bg='light grey')
welcome_label.place(x=200, y=0)

time_label = Label(options_top, text="", font=('Bold', 7), fg = 'Black',bg='light grey')
time_label.place(x=420, y=0)

# Buttons
Home_button = Button(options_top, text='Home', font=('Arial', 13),
                     bd=0, fg='#0097e8', bg='light grey', activeforeground='grey',
                     command=lambda: indicate(Home_indicate, home_page))
Home_button.place(x=0, y=20, width=125)

Home_indicate = Label(options_top, text="", bg='light grey')
Home_indicate.place(x=45, y=50, width=35, height=5)

Tasks_button = Button(options_top, text='Tasks', font=('Arial', 13),
                      bd=0, fg='#0097e8', bg='light grey', activeforeground='grey',
                      command=lambda: indicate(Tasks_indicate, task_page))
Tasks_button.place(x=125, y=20, width=125)

Tasks_indicate = Label(options_top, text="", bg='light grey')
Tasks_indicate.place(x=170, y=50, width=35, height=5)

TBC_button = Button(options_top, text='TBC', font=('Arial', 13),
                    bd=0, fg='#0097e8', bg='light grey', activeforeground='grey',
                    command=lambda: indicate(TBC_indicate, tbc_page))
TBC_button.place(x=250, y=20, width=125)

TBC_indicate = Label(options_top, text="", bg='light grey')
TBC_indicate.place(x=297, y=50, width=35, height=5)

Settings_button = Button(options_top, text='Settings', font=('Arial', 13),
                         bd=0, fg='#0097e8', bg='light grey', activeforeground='grey',
                         command=lambda: indicate(Settings_indicate, settings_page))
Settings_button.place(x=375, y=20, width=125)

Settings_indicate = Label(options_top, text="", bg='light grey')
Settings_indicate.place(x=420, y=50, width=35, height=5)

indicate(Home_indicate, home_page)

update_time()
window.mainloop()
