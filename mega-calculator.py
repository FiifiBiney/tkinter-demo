"""
THIS IS A MEGA-CALCULATOR APP THAT IS MEANT TO REGISTER MOUSE CLICK AND KEYBOARD HITS
"""

#Importing the tkinter module
from tkinter import *

#Creating the Window
win = Tk()

#We dont want the Windw to be resizable
win.resizable(0, 0)

#Giving a geometry to our Window
win.geometry("400x400")

#Title of the Application
win.title("MEGA-CALCULATOR")

#Defining all our needed functions to make the Calculator work effectively
#Creating a button to update our tezt field anytie a number is keyed in or any button is pressed
def btnClick( item ):
    global expression #Using global to expose the expression variable outside of the function
    expression += str( item )
    txtExpression.set( expression )

#Creating a button to clear the data on the textfield
def btnClear():
    global expression #Using global to expose the expression variable outside of the function
    expression = ""
    txtExpression.set( expression )

#Creating an equal to button to calculate whatever expression is given in the field
def btnEqual():
    global expression #Using global to expose the expression variable outside of the function
    result = str( eval(expression) ) #Using eval to evaluate the expression in string
    txtExpression.set( result )
    expression = ""

expression = ""
txtExpression = StringVar() #Create an instance of the text field

#Designing the layout of the calculator
txtFrame = Frame( win, width = 400, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
txtFrame.pack( side = TOP )

#Setting the input field for calculator and aligning it to the right
txtField = Entry( txtFrame, font = ('arial', 18, "bold"), textvariable = txtExpression, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
txtField.grid( row = 0, column = 0 ) #Setting it to the very first row and column
txtField.pack( ipady = 10 ) #ipady increases the height for us by the number we set

#Creating a frame to hold all buttons
btnsFrame = Frame( win, width = 400, height = 280, bg = "grey" )
btnsFrame.pack()

#Setting the clear and divide buttons on the first row
btnClear = Button( btnsFrame, text = "C", fg = "black", width = 34, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btnClear() )
btnClear.grid( row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

btnDivide = Button( btnsFrame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btnClick("/") )
btnDivide.grid( row = 0, column = 3, padx = 1, pady = 1 )

#Setting the 7, 8, 9 and * buttons which will be on the second row
btnSeven = Button( btnsFrame, text = "7", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command =lambda: btnClick( 7 ) )
btnSeven.grid( row = 1, column = 0, padx = 1, pady = 1 )

btnEight = Button( btnsFrame, text = "8", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command =lambda: btnClick( 8 ) )
btnEight.grid( row = 1, column = 1, padx = 1, pady = 1 )

btnNine = Button( btnsFrame, text = "9", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command =lambda: btnClick( 9 ) )
btnNine.grid( row = 1, column = 2, padx = 1, pady = 1 )

btnMultiply = Button( btnsFrame, text = "*", fg = "black", width = 10, height = 3, bg = "#eee", cursor = "hand2", command =lambda: btnClick( "*" ) )
btnMultiply.grid( row = 1, column = 3, padx = 1, pady = 1 )

#Setting the 4, 5, 6 and - buttons which will be on the third row
btnFour = Button( btnsFrame, text = "4", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command =lambda: btnClick( 4 ) )
btnFour.grid( row = 2, column = 0, padx = 1, pady = 1 )

btnFive = Button( btnsFrame, text = "5", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command =lambda: btnClick( 5 ) )
btnFive.grid( row = 2, column = 1, padx = 1, pady = 1 )

btnSix = Button( btnsFrame, text = "6", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command =lambda: btnClick( 6 ) )
btnSix.grid( row = 2, column = 2, padx = 1, pady = 1 )

btnMinus = Button( btnsFrame, text = "-", fg = "black", width = 10, height = 3, bg = "#eee", cursor = "hand2", command =lambda: btnClick( "-" ) )
btnMinus.grid( row = 2, column = 3, padx = 1, pady = 1 )

#Setting the 1, 2, 3 and + buttons which will be on the fourth row
btnOne = Button( btnsFrame, text = "1", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command =lambda: btnClick( 1 ) )
btnOne.grid( row = 3, column = 0, padx = 1, pady = 1 )

btnTwo = Button( btnsFrame, text = "2", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command =lambda: btnClick( 2 ) )
btnTwo.grid( row = 3, column = 1, padx = 1, pady = 1 )

btnThree = Button( btnsFrame, text = "3", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command =lambda: btnClick( 3 ) )
btnThree.grid( row = 3, column = 2, padx = 1, pady = 1 )

btnPlus = Button( btnsFrame, text = "+", fg = "black", width = 10, height = 3, bg = "#eee", cursor = "hand2", command =lambda: btnClick( "+" ) )
btnPlus.grid( row = 3, column = 3, padx = 1, pady = 1 )

#Setting the 0, ., and = buttons which will be on the fifth row
btnZero = Button( btnsFrame, text = "0", fg = "black", width = 22, height = 3, bg = "#fff", cursor = "hand2", command =lambda: btnClick( 0 ) )
btnZero.grid( row = 4, column = 0, columnspan = 2, padx = 1, pady = 1 )

btnDot = Button( btnsFrame, text = ".", fg = "black", width = 10, height = 3, bg = "#eee", cursor = "hand2", command =lambda: btnClick( "." ) )
btnDot.grid( row = 4, column = 2, padx = 1, pady = 1 )

btnEqualto = Button( btnsFrame, text = "=", fg = "black", width = 10, height = 3, bg = "#eee", cursor = "hand2", command =lambda: btnEqual( ))
btnEqualto.grid( row = 4, column = 3, padx = 1, pady = 1 )

win.mainloop() #Creating our loop
