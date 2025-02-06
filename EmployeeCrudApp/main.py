from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.geometry("600x270")
window.title("Employee CRUD App")

def insert_data():
    id = enter_emp_id.get()
    name = enter_emp_name.get()
    dept = enter_emp_dept.get()

    if id == "" or name == "" or dept == "":
        messagebox.showerror("Error", "All fields are required")
        return
    else:
        conn = mysql.connector.connect(
            host="localhost", user="root", database="employee")
        myCursor = conn.cursor()
        myCursor.execute(
            "INSERT INTO emp_details VALUES('"+id+"','"+name+"','"+dept+"')")
        conn.commit()

        # Clear Values
        reset_fields()

        messagebox.showinfo("Success", "Data inserted successfully")
        conn.close()
        show()


def update_data():
    id = enter_emp_id.get()
    name = enter_emp_name.get()
    dept = enter_emp_dept.get()

    if id == "" or name == "" or dept == "":
        messagebox.showerror("Error", "All fields are required")
        return
    else:
        conn = mysql.connector.connect(
            host="localhost", user="root", database="employee")
        myCursor = conn.cursor()
        myCursor.execute(
            "UPDATE emp_details SET emp_name='"+name+"', emp_dept='"+dept+"' WHERE emp_id='"+id+"'"
        )
        conn.commit()

        # Clear Values
        reset_fields()
        show()

        messagebox.showinfo("Update Status", "Data updated successfully")
        conn.close()


def get_data():
    id = enter_emp_id.get()

    if id == "":
        messagebox.showerror("Error", "Employee ID is required")
        return
    else:
        conn = mysql.connector.connect(
            host="localhost", user="root", database="employee")
        myCursor = conn.cursor()
        myCursor.execute(
            "SELECT * FROM emp_details WHERE emp_id='"+id+"'")
        rows = myCursor.fetchall()

        for row in rows:
            enter_emp_name.insert(0, row[1])
            enter_emp_dept.insert(0, row[2])

        conn.close()


def delete_data():
    id = enter_emp_id.get()

    if id == "":
        messagebox.showerror("Error", "Employee ID is required")
        return
    else:
        conn = mysql.connector.connect(
            host="localhost", user="root", database="employee")
        myCursor = conn.cursor()
        myCursor.execute(
            "DELETE FROM emp_details WHERE emp_id='"+id+"'")
        conn.commit()

        # Clear Values
        reset_fields()

        messagebox.showinfo("Delete Status", "Data deleted successfully")
        conn.close()
        show()


def show():
    conn = mysql.connector.connect(
        host="localhost", user="root", database="employee")
    myCursor = conn.cursor()
    myCursor.execute("SELECT * FROM emp_details")
    rows = myCursor.fetchall()
    show_data.delete(0, show_data.size())

    for row in rows:
        add_data = str(row[0]) + " " + row[1] + " " + row[2]
        show_data.insert(show_data.size() + 1, add_data)

    conn.close()


def reset_fields():
    enter_emp_id.delete(0, 'end')
    enter_emp_name.delete(0, 'end')
    enter_emp_dept.delete(0, 'end')


emp_id = Label(window, text="Employee ID", font=("Serif", 12))
emp_id.place(x=20, y=30)

emp_name = Label(window, text="Employee Name", font=("Serif", 12))
emp_name.place(x=20, y=60)

emp_dept = Label(window, text="Employee Dept", font=("Serif", 12))
emp_dept.place(x=20, y=90)

enter_emp_id = Entry(window)
enter_emp_id.place(x=170, y=30)

enter_emp_name = Entry(window)
enter_emp_name.place(x=170, y=60)

enter_emp_dept = Entry(window)
enter_emp_dept.place(x=170, y=90)

insert_button = Button(
    window, text="Insert", font=("Sans", 12), bg="white", command=insert_data
)
insert_button.place(x=20, y=160)

update_button = Button(
    window, text="Update", font=("Sans", 12), bg="white", command=update_data
)
update_button.place(x=80, y=160)

get_button = Button(
    window, text="Fetch", font=("Sans", 12), bg="white", command=get_data
)
get_button.place(x=150, y=160)

delete_button = Button(
    window, text="Delete", font=("Sans", 12), bg="white", command=delete_data
)
delete_button.place(x=210, y=160)

reset_button = Button(
    window, text="Reset", font=("Sans", 12), bg="white", command=reset_fields
)
reset_button.place(x=20, y=210)

show_data = Listbox(window)
show_data.place(x=330, y=30)
show()

window.mainloop()
