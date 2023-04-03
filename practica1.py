from tkinter import *
from tkinter import messagebox
import sqlite3

#------------------------ Functions ------------------------
def connectionbbdd():
    myconecction=sqlite3.connect("Users ")

    mycursor=myconecction.cursor()

    try:

        mycursor.execute(''' 
            CREATE TABLE USERDATA (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USER_NAME VARCHAR(50),
            PASSWORD VARCHAR(50),
            LASTNAME VARCHAR(15),
            ADDRESS VARCHAR(50),
            COMMENTS VARCHAR(280))
            ''')

        messagebox.showinfo("BBDD", "Database created successfully")


    except:
        
        messagebox.showwarning("¡attention!", "The database already exists")

def exitapp():
    question=messagebox.askquestion("Exit", "Do you want to exit the application?")

    if question=="yes":
        root.destroy()
    
def clear():
    my_name.set("")
    my_id.set("")
    my_address.set("")
    my_lastname.set("")
    my_pass.set("")
    frame_text.delete(1.0,END)
#------------------------ End of functions ------------------------
#------------------------ CRUD Functions ------------------------
def create():
    my_conecction=sqlite3.connect("Users ")

    my_cursor=my_conecction.cursor()

    data=my_name.get(),my_pass.get(),my_lastname.get(),my_address.get(),frame_text.get("1.0", END)

    #my_cursor.execute("INSERT INTO USERDATA VALUES(NULL, ' " + my_name.get() + 
    #                  "','" + my_pass.get() + 
    #                  "','" + my_lastname.get() + 
    #                  "','" + my_address.get() + 
    #                  "','" + frame_text.get("1.0", END) + " ')")
    #my_conecction.commit()

    my_cursor.execute("INSERT INTO USERDATA VALUES(NULL,?,?,?,?,?)",(data))
    my_conecction.commit()

    messagebox.showinfo("BBDD", "Record inserted successfully" )

def read():

    my_connection=sqlite3.connect("Users ")
    my_cursor=my_connection.cursor()

    my_cursor.execute("SELECT * FROM USERDATA WHERE ID="+my_id.get())

    the_user=my_cursor.fetchall()
    
    for user in the_user:
        my_id.set(user[0])
        my_name.set(user[1])
        my_pass.set(user[2])
        my_lastname.set(user[3])
        my_address.set(user[4])
        frame_text.insert(1.0, user[5])

    my_connection.commit()


def update():
    my_connection=sqlite3.connect("Users ")
    my_cursor= my_connection.cursor()
    data=my_name.get(),my_pass.get(),my_lastname.get(),my_address.get(),frame_text.get("1.0", END)
    #my_cursor.execute("UPDATE USERDATA SET USER_NAME='" + my_name.get() +
    #                  "', PASSWORD='" + my_pass.get() +
    #                  "', LASTNAME='" + my_lastname.get() +
    #                  "', ADDRESS='" + my_address.get() +
    #                  "', COMMENTS='" + frame_text.get("1.0", END) +
    #                  "' WHERE ID=" + my_id.get())
    my_cursor.execute("UPDATE USERDATA SET USER_NAME=?, PASSWORD=?, LASTNAME=?, ADDRESS=?, COMMENTS=? "+ "WHERE ID=" +my_id.get(),(data) )
    my_connection.commit()
    
    messagebox.showinfo("BBDD", "Update done successfully" )

def delete():
    my_connection=sqlite3.connect("Users ")

    my_cursor=my_connection.cursor()

    my_cursor.execute("DELETE FROM USERDATA WHERE ID=" +my_id.get())

    my_connection.commit()

    messagebox.showinfo("BBDD", "The information was removed")


#------------------------ End CRUD of functions ------------------------


root=Tk()

#------------------------ navigation bar buttons ------------------------
navigation_bar=Menu(root)
root.config(menu=navigation_bar, width=300, height=300)

bbdd_menu=Menu(navigation_bar, tearoff=0)
bbdd_menu.add_command(label="Connect", command=connectionbbdd)
bbdd_menu.add_command(label="Disconnect", command=exitapp)

delete_menu=Menu(navigation_bar, tearoff=0)
delete_menu.add_command(label="Delete fields", command=clear)

crud_menu=Menu(navigation_bar, tearoff=0)
crud_menu.add_command(label="Create ", command=create)
crud_menu.add_command(label="Read", command=read)
crud_menu.add_command(label="Update", command=update)
crud_menu.add_command(label="Delete",command=delete)

help_menu=Menu(navigation_bar,tearoff=0)
help_menu.add_command(label="License")
help_menu.add_command(label="about...")

navigation_bar.add_cascade(label="BBDD", menu=bbdd_menu)
navigation_bar.add_cascade(label="Delete", menu=delete_menu)
navigation_bar.add_cascade(label="CRUD", menu=crud_menu)
navigation_bar.add_cascade(label="Help", menu=help_menu)

#------------------------ menu fields ------------------------

main_frame=Frame(root)
main_frame.pack()

my_id=StringVar()
my_name=StringVar()
my_pass=StringVar()
my_lastname=StringVar()
my_address=StringVar()


frame_id=Entry(main_frame, textvariable=my_id)
frame_id.grid(row=0, column=1, padx=10, pady=10)

frame_name=Entry(main_frame, textvariable=my_name)
frame_name.grid(row=1, column=1, padx=10, pady=10)
frame_name.config(fg="red", justify="right")

frame_pass=Entry(main_frame, textvariable=my_pass)
frame_pass.grid(row=2, column=1, padx=10, pady=10)
frame_pass.config(show="*")

frame_lastname=Entry(main_frame,textvariable=my_lastname)
frame_lastname.grid(row=3, column=1, padx=10, pady=10)

frame_address=Entry(main_frame,textvariable=my_address)
frame_address.grid(row=4, column=1, padx=10, pady=10)

frame_text=Text(main_frame, width=16, height=5)
frame_text.grid(row=5, column=1,padx=10, pady=10)
scrollVert=Scrollbar(main_frame, command=frame_text.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

frame_text.config(yscrollcommand=scrollVert.set)

#------------------------ Labels start here ------------------------

id_label=Label(main_frame, text="ID: ")
id_label.grid(row=0,column=0, sticky="e",padx=10,pady=10)

name_label=Label(main_frame, text="Name: ")
name_label.grid(row=1, column=0, sticky="e",padx=10, pady=10)

pass_label=Label(main_frame, text="Password: ")
pass_label.grid(row=2, column=0,sticky="e",padx=10, pady=10)

lastname_label=Label(main_frame, text="Last name: ")
lastname_label.grid(row=3, column=0, sticky="e",padx=10, pady=10)

address_label=Label(main_frame, text="Address: ")
address_label.grid(row=4, column=0, sticky="e", padx=10, pady=10)

text_label=Label(main_frame, text="Text: ")
text_label.grid(row=5, column=0, sticky="e", padx=10, pady=10)


#------------------------ The buttons of the crud ------------------------

second_frame=Frame(root)
second_frame.pack()

button_create=Button(second_frame, text="Create", command=create)
button_create.grid(row=1, column=0, sticky="e", padx=10,pady=10)

button_read=Button(second_frame, text="Read", command=read)
button_read.grid(row=1, column=1, sticky="e", padx=10, pady=10)

button_update=Button(second_frame, text="Update",command=update)
button_update.grid(row=1, column=2, sticky="e", padx=10, pady=10)

button_delete=Button(second_frame, text="Delete",command=delete)
button_delete.grid(row=1, column=3, sticky="e", padx=10, pady=10)



root.mainloop()