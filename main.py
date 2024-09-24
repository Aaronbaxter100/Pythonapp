from tkinter import*

window = Tk()
window.geometry('500x500')
window.title('Testing')


options_top = Frame(window, bg= 'blue')
options_top.pack(pady=5)
options_top.pack_propagate(False)
options_top.configure(width=500, height= 55)

#Labels
#label1 = Label(text = ('Testingwelcome'), font = ('Arial', 30))
#label1.pack()

#Frames
#left_frame = Frame(window, bg=blue)
#left_frame.grid()

window.mainloop()