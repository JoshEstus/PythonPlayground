from tkinter import *

window = Tk()

lbl = Label(window, text="Choose your favourite programming languages:")
frame = Frame(window)

python = Checkbutton(frame, text="Python")
java = Checkbutton(frame, text="Java")
js = Checkbutton(frame, text="JavaScript")
cpp =  Checkbutton(frame, text="C++")
ruby = Checkbutton(frame, text="Ruby")

lbl.pack()
frame.pack()
python.pack()
java.pack()
js.pack()
cpp.pack()
ruby.pack()

window.mainloop()