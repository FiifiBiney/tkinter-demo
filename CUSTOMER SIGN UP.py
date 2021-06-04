#Importing tkinter for our interface design

import tkinter as tk #using the alias tk instead of the normal tkinter 
from tkinter import ttk

#Create an instance of tk
win = tk.Tk()

#Giving window a title
win.title( 'CUSTOMER SIGN-UP FORM' )

#Creating an empty space
ttk.Label(win).grid(row = 0)

#Setting our username labels and input boxes
lblUserName = ttk.Label(win, text="Username: ") 
lblUserName.grid(column = 1, row = 1)

#Creating an empty space
ttk.Label(win).grid(row = 2)

#Setting our username textbox
name = tk.StringVar()
txtUserName = ttk.Entry(win, width = 16, textvariable=name)
txtUserName.grid(column = 3, row = 1)

#Setting our Email labels and input boxes
lblEmail = ttk.Label(win,text = "Email: ")
lblEmail.grid(column = 1, row = 3)

#Setting our email textbox
email = tk.StringVar()
txtEmail = ttk.Entry(win, width = 25, textvariable=email)
txtEmail.grid(column = 3, row = 3)

#Creating an empty space
ttk.Label(win).grid(row = 4)

#Setting our Password labels and input boxes
lblPassword = ttk.Label(win, text = "Password: ")
lblPassword.grid(column = 1, row = 5)

#Setting our Password textbox
Password = tk.StringVar()
txtPassword = ttk.Entry(win, width = 20, textvariable=Password)
txtPassword.grid(column = 3, row = 5)

#Creating an empty space
ttk.Label(win).grid(row = 0)

#Setting our submit button
btnSubmit = ttk.Button(win, width = 15, text="Submit")
btnSubmit.grid(column = 3, row = 7)

#Invoking the GUI Loop
win.mainloop()