from tkinter import *
from PIL import ImageTk, Image

# Create container window
window = Tk()


name = Label(window, text="Hello World", bg="white", fg="blue", font=("Serif", 16))
img = Image.open('python.png')
logo = ImageTk.PhotoImage(Image.open("python.png"))
image = Label(window, image=logo)

button = Button(window, text="Let's Start")

username = Label(window, text="Username", font=("Serif", 12))
inputBox = Entry(window)


name.pack()
image.pack()
username.pack(side=LEFT)
inputBox.pack(side=RIGHT)
# Will have to resize window a bit to see
button.place(x=100, y=350)
window.mainloop()
