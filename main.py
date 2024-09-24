from tkinter import *

window = Tk()
window.geometry('500x500')
window.title('Testing')

# Frames
options_top = Frame(window, bg= 'blue')
options_top.pack(pady=5)
options_top.pack_propagate(False)
options_top.configure(width=500, height= 55)

# Buttons
Home_button = Button(options_top, text='Home', font =('Arial',13),
                     bd=0, fg= '#0097e8', activeforeground= '#0097e8')
Home_button.place(x=0, y=0, width=125)

Tasks_button = Button(options_top, text='Tasks', font =('Arial',13),
                     bd=0, fg= '#0097e8', activeforeground= '#0097e8')
Tasks_button.place(x=125, y=0, width=125)

# left_frame = Frame(window, bg=blue)
# left_frame.grid()

# Labels
# label1 = Label(text = ('Testing welcome'), font = ('Arial', 30))
# label1.pack()


window.mainloop()