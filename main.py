from os.path import commonpath
from tkinter import *
from tkinter import ttk
import time

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

    test1 = Button(home_frame, text = 'Testing One', font =('Bold,40'))
    test1.grid(row = 2, column = 0, sticky='w')

    test2 = Button(home_frame, text='Testing Two', font=('Bold,40'),)
    test2.grid(row=3, column=0, sticky='w')

    #active = Label(home_frame, text='Active Tasks', font=('Bold', 30), bg='pink')
    #active.grid(row=1, column=0, sticky='w')

    home_frame.pack(pady=20)

def task_page():
    task_frame = Frame(main_frame)

    lb = Label(task_frame, text='Task page\n\nPage: 2', font=('Bold', 30), bg = 'pink')
    lb.pack()

    task_frame.pack()


def tbc_page():
    tbc_frame = Frame(main_frame)

    lb = Label(tbc_frame, text='TBC\n\nPage: 3', font=('Bold', 30),bg = 'pink')
    lb.pack()

    tbc_frame.pack(pady=20)

def settings_page():

    settings_frame = Frame(main_frame)
    settings_frame.pack(fill='both', expand=True)


    button_frame = Frame(settings_frame)
    button_frame.pack(side='left', fill='y', padx=10, pady=10)


    button1 = Button(button_frame, text='Button 1')
    button1.pack(pady=5)

    button2 = Button(button_frame, text='Button 2')
    button2.pack(pady=5)

    help = Button(button_frame, text='Help')
    help.pack(pady=5)

    theme_options = ['Light Mode', 'Dark Mode']
    theme_dropdown = ttk.Combobox(button_frame, values=theme_options, state='readonly')
    theme_dropdown.set('Light Mode')
    theme_dropdown.pack(pady=10)


    lb = Label(settings_frame, text='Settings Page\n\nPage: 4', font=('Bold', 30), bg='pink')
    lb.pack(pady=10)

    def on_theme_change(event):
        selected_theme = theme_dropdown.get()
        apply_theme(selected_theme)

    theme_dropdown.bind('<<ComboboxSelected>>', on_theme_change)

    settings_frame.pack(pady=20)

def help()
    commonpath()


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

# Frames
options_top = Frame(window, bg='light grey')
options_top.pack(pady=5)
options_top.pack_propagate(False)
options_top.configure(width=500, height=55)

main_frame = Frame(window, bg='pink')
main_frame.pack(pady=5)
main_frame.pack_propagate(False)
main_frame.configure(width=500, height=700)

# Labels
time_label = Label(options_top, text="", font=('Arial', 8), bg='light grey')
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
