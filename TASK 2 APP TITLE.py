#Importing tkinter for our interface design

import tkinter as tk #using the alias tk instead of the normal tkinter 
from tkinter import ttk
from tkinter.ttk import *

#Create an instance of tk
win = tk.Tk()

#Giving window a title
win.title( 'APP TITLE' )
ttk.Label(win).grid(column = 0)

#Creating an empty space
ttk.Label(win).grid(row = 0)

#Setting our FNAME labels and input boxes
lblFNAME = ttk.Label(win, text="FNAME: ") 
lblFNAME.grid(column = 1, row = 1)

#Creating an empty space
ttk.Label(win).grid(row = 2)

#Setting our FNAME textbox
fName = tk.StringVar()
txtFNAME = ttk.Entry(win, width = 16, textvariable=fName)
txtFNAME.grid(column = 3, row = 1)

#Setting our LNAME labels and input boxes
lblLNAME = ttk.Label(win,text = "LNAME: ")
lblLNAME.grid(column = 1, row = 3)

#Creating an empty space
ttk.Label(win).grid(row = 4)

#Setting our LNAME textbox
lName = tk.StringVar()
txtLNAME = ttk.Entry(win, width = 16, textvariable=lName)
txtLNAME.grid(column = 3, row = 3)

#Setting our EMAIL labels and input boxes
lblEMAIL = ttk.Label(win,text = "EMAIL: ")
lblEMAIL.grid(column = 1, row = 5)

#Creating an empty space
ttk.Label(win).grid(row = 6)

#Setting our EMAIL textbox
email = tk.StringVar()
txtEMAIL = ttk.Entry(win, width = 16, textvariable=email)
txtLNAME.grid(column = 3, row = 5)

#Setting our PASSWORD labels and input boxes
lblPASSD = ttk.Label(win, text = "PASSD: ")
lblPASSD.grid(column = 1, row = 7)

#Creating an empty space
ttk.Label(win).grid(row = 8)

#Setting our PASSWORD textbox
passd = tk.StringVar()
txtPASSD = ttk.Entry(win, width = 16, textvariable=passd)
txtPASSD.grid(column = 3, row = 7)



#Setting our SUBMIT button
btnSUBMIT = ttk.Button(win, style = "W.TButton", width = 10, text="SUBMIT")
btnSUBMIT.config( bg="#00FF00" )
btnSUBMIT.grid(column = 1, row = 9)
# btnSUBMIT.configure(background="#00FFF00")

#Setting our RESET button
btnRESET = ttk.Button(win, width = 16, text="RESET")
btnRESET.grid(column = 3, row = 9)
# btnRESET.configure(background="#FF0000") 

#Invoking the GUI Loop
win.mainloop()
