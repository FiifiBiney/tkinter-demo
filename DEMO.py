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

#Starting up our textfield event
def click_me():
    text_action.configure( text = "Hello "  + Name.get() ) #Dispalying the user's name


#Setting our text label
lblText = ttk.Label( window, text = "Please enter a name", padding = 3, )
lblText.grid( column = 0, row = 2 )

#Adding the textbox widget
Name = tk.StringVar ()
user_name = ttk.Entry( window, width = 14, textvariable = Name )
user_name.grid( column = 0, row = 3 )
user_name.focus() #Placing the cursor to focus on this textbox

#Adding our button
action = ttk.Button( window, text = "Open Sesame!", command = reveal_me ) #Activating the button
action.grid( column = 1, row = 0 )
action.configure( state = "disabled") #Disabling the button

#Adding our text button
text_action = ttk.Button( window, text = "Click to greet", command = click_me )
text_action.grid( column = 1, row = 3 )

#Starting the GUI
window.mainloop()