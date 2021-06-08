#Importing our tkinter Module
from tkinter import *
from tkinter.ttk import Combobox #Importing Combobox
#Create an instance of the Tk window
win = Tk()

numbers = ( "One", "Five", "Eleven", "Twelve", "Sixteen" )

#Creating our Listbox
lbListbox = Listbox( win, height = 5, selectmode = "multiple" )

#Looping through the numbers one by one to be used in the listbox
for number in numbers:
    lbListbox.insert( END, number )

lbListbox.place(x=250, y=150)

#Creating our Combobox
data = StringVar() #Variable to record selection or inputs
data.set( numbers[0] ) #Taking the first valuuein the numbers tuple variable.

cbCombobox = Combobox( win, value = numbers ) #Inserting the values for the Combox
cbCombobox.place( x = 60, y = 150 )

#Creating a checkbutton
check1_value = IntVar() #Creating a variable to hold integer values
check2_value = IntVar()

cb1Checkbox = Checkbutton( win, text = "Guava", variable = check1_value)
cb2Checkbox = Checkbutton( win, text = "Orange", variable = check2_value)

cb1Checkbox.place( x = 70, y = 100)
cb2Checkbox.place( x = 130, y = 100)

#Creating a radio button
rb_value = IntVar()
rb_value.set( 1 )

rb1_Radiobutton = Radiobutton( win, text = "Male", variable = rb_value, value=1)
rb2_Radiobutton = Radiobutton( win, text = "Female", variable = rb_value, value=2)
rb1_Radiobutton.place(x=70, y=50)
rb2_Radiobutton.place(x=130, y=50)

win.title( "Checklist App" )
win.geometry( "400x300+10+10" )
win.mainloop()