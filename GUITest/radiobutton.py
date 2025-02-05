from tkinter import *

window = Tk()

lbl = Label(window, text="Sun or Moon:")
var = StringVar()
sun = Radiobutton(window, text="Sun", variable=var, value="S")
moon = Radiobutton(window, text="Moon", variable=var, value="M")
lbl.pack()
sun.pack()
moon.pack()

window.mainloop()