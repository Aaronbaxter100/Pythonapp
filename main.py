from tkinter import*

window = Tk()
window.geometry('400x400')
window.title('Testing')

#Labels
label1 = Label(text = ('Testingwelcome'), font = ('Arial', 30))
label1.pack()

#Frames
left_frame = Frame(window, bg=blue)
left_frame.grid()

window.mainloop()