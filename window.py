#Importing tkinter for our interface design

import tkinter as tk #using the alias tk instead of the normal tkinter 
from tkinter import ttk

#Create an instance of tk
window = tk.Tk()

#Giving window a title
window.title( 'Our Demo App' )

#Restricting window resizing
window.resizable( True, True ) #x, y

#Introducing our first label
#ttk.Label( window, text = "Guess my name" ).grid( column = 0, row = 0 )
lblName = ttk.Label( window, text = "Guess my name" )
lblName.grid( column = 0, row = 0 )

#Starting our button up for an event
def reveal_me ():
    action.configure( text = "Mystery Solved!" ) #Text that replaces "Guess my name"
    lblName.configure( foreground = "blue") #Colour of the text
    lblName.configure( text = "Benjamin Benson") #Name revealed

#Adding our button
action = ttk.Button( window, text = "Open Sesame!", command = reveal_me ) #Activating the button
action.grid( column = 1, row = 0 )

#Starting the GUI
window.mainloop()