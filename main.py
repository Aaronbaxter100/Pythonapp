from tkinter import *

window = Tk()
window.geometry('500x500')
window.title('Testing')

def home_page():
    home_frame = Frame(window)

    lb = Label(home_frame,text='Home page\n\nPage: 1', font =('Bold', 30))
    lb.pack()

    home_frame.pack(pady=20)

def task_page():
    task_frame = Frame(window)

    lb = Label(task_frame,text='Task page\n\nPage: 2', font =('Bold', 30))
    lb.pack()

    task_frame.pack(pady=20)

def TBC_page():
    TBC_frame = Frame(window)

    lb = Label(TBC_frame,text='Unsure page\n\nPage: 3', font =('Bold', 30))
    lb.pack()

    TBC_frame.pack(pady=20)

def settings_page():
    settings_frame = Frame(window)

    lb = Label(settings_frame,text='settings page\n\nPage: 4', font =('Bold', 30))
    lb.pack()

    settings_frame.pack(pady=20)



def hide_indicators():
    Home_indicate.config(bg='light grey')
    Tasks_indicate.config(bg='light grey')
    TBC_indicate.config(bg='light grey')
    Settings_indicate.config(bg='light grey')

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='Blue')
    page()


# Frames
options_top = Frame(master=window, bg= 'light grey')
options_top.pack(pady=5)
options_top.pack_propagate(False)
options_top.configure(width=500, height= 55)

# Buttons
Home_button = Button(options_top, text='Home', font =('Arial',13),
                    bd=0, fg= '#0097e8', bg='light grey' ,activeforeground= 'grey',
                    command=lambda: indicate(Home_indicate, home_page()))

Home_button.place(x=0, y=0, width=125)

Home_indicate = Label(options_top, text="", bg='light grey')
Home_indicate.place(x=45, y=30, width=35, height=5)

Tasks_button = Button(options_top, text='Tasks', font =('Arial',13),
                     bd=0, fg= '#0097e8',bg='light grey', activeforeground= 'grey',
                    command=lambda: indicate(Tasks_indicate,task_page()))

Tasks_button.place(x=125, y=0, width=125)

Tasks_indicate = Label(options_top, text="", bg='light grey')
Tasks_indicate.place(x=170, y=30, width=35, height=5)

TBC_button = Button(options_top, text='Unsure', font =('Arial',13),
                    bd=0, fg= '#0097e8', bg='light grey', activeforeground= 'grey',
                    command=lambda: indicate(TBC_indicate, TBC_page()))

TBC_button.place(x=250, y=0, width=125)

TBC_indicate = Label(options_top, text="", bg='light grey')
TBC_indicate.place(x=297, y=30, width=35, height=5)

Settings_button = Button(options_top, text='Settings', font =('Arial',13),
                    bd=0, fg= '#0097e8',bg='light grey', activeforeground= 'grey',
                    command=lambda: indicate(Settings_indicate, settings_page()))

Settings_button.place(x=375, y=0, width=125)

Settings_indicate = Label(options_top, text="", bg='light grey')
Settings_indicate.place(x=420, y=30, width=35, height=5)

# left_frame = Frame(window, bg=blue)
# left_frame.grid()

# Labels
# label1 = Label(text = ('Testing welcome'), font = ('Arial', 30))
# label1.pack()


window.mainloop()