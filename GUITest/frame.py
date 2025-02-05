from tkinter import *

window = Tk()

frame = Frame(window)

label = Label(frame, text="Inside The Frame")
button = Button(frame, text="Insde the Frame")
frame.pack()
label.pack(side=TOP)
button.pack(side=BOTTOM)
window.mainloop()