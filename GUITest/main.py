from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def showMessage():
    messagebox.showinfo("Welcome to PythonX", "Welcome")


def gui():

    def greetUser(event):
        username = inputBox.get()
        greet["text"] = "Hello " + username


    window = Tk()
    name = Label(window, text="PythonX - Learn Python", bg="white", fg="blue", font=("Serif", 16))
    img = Image.open("python.png")
    logo = ImageTk.PhotoImage(img)
    image = Label(window, image=logo)

    frame = Frame(window)
    username = Label(frame, text="Username:", bg="white", fg="black", font=("Serif", 12))
    inputBox = Entry(frame)
    button = Button(window, text="Lets Start", command=showMessage)
    bindButton = Button(window, text="Greet")
    bindButton.bind("<Button-1>", greetUser)
    greet = Label(window)

    name.pack()
    image.pack()
    frame.pack()
    username.pack(side=LEFT)
    inputBox.pack(side=RIGHT)
    button.pack(side=BOTTOM)
    bindButton.pack(side=BOTTOM)
    greet.pack()

    window.mainloop()


if __name__ == "__main__":
    gui()