"""
THIS IS A MINI-CALCULATOR APP THAT IS MEANT TO REGISTER MOUSE CLICK AND KEYBOARD HITS
"""

#Importing the tkinter module
from tkinter import *

class OurWindow:
    def __init__(self, win):
        self.lblFnum = Label( win, text = "First Number" )
        self.lblFnum.place( x = 100, y = 50 ) #Setting the position for the First Number label
        self.lblSnum = Label( win, text = "Second Number" )
        self.lblSnum.place( x = 100, y = 100 ) #Setting the position for the Second Number label
        self.lblResult = Label( win, text = "Result")
        self.lblResult.place( x = 100, y = 200 )

        #Setting up our Textboxes (Entry fields)
        self.txtFnum = Entry()
        self.txtFnum.place( x = 200, y = 50 ) #Setting up the position for First Number Entry Field
        self.txtSnum = Entry()
        self.txtSnum.place( x = 200, y = 100 ) #Setting up the position for Second Number Entry Field
        self.txtResult = Entry( bd = 3 ) #Giving the Result textbox a border width of 3
        self.txtResult.place( x = 200, y = 200 ) #Setting up the position for Result Entry Field

        #Setting up our Buttons
        self.btnAdd = Button( win, text = "Add", command = self.add )
        self.btnAdd.place( x = 100, y = 150 ) #Setting up the position for the Add Button
        self.btnSubtract = Button( win, text = "Subtract", command = self.sub )
        self.btnSubtract.place( x = 200, y = 150 ) #Setting up the position for the Subtract Button

    #Defining our addition event
    def add(self):
        self.txtResult.delete( 0, 'end' )
        firstNumber= int( self.txtFnum.get() ) #Grabbing the input from the First Number
        secondNumber= int( self.txtSnum.get() ) #Grabbing the input from the Second Number

        result = firstNumber + secondNumber #Performing the addition

        self.txtResult.insert( END, str( result ) )

    #Defining our Subtraction event
    def sub(self):
        self.txtResult.delete( 0, 'end' )
        firstNumber= int( self.txtFnum.get() ) #Grabbing the input from the First Number
        secondNumber= int( self.txtSnum.get() ) #Grabbing the input from the Second Number

        result = firstNumber - secondNumber #Performing the Subtraction

        self.txtResult.insert( END, str( result ) )

#Setting up the window
container = Tk()
myContainer = OurWindow( container )
container.title("Mini-Calculator" )
container.geometry("400x300+10+10")
container.mainloop()
