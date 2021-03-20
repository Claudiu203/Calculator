from tkinter import*

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()

#Display

txtDisplay = Entry(cal,font = ('arial',20,"bold") , textvariable = text_Input , bd=30 , insertwidth = 4 , bg = "powder blue" , justify = "right").grid(columnspan = 4)

#-----------------------------------First row-----------------------------------

#Button 7

btn7 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black" , font = ('arial',20,"bold"), text = "7", command = lambda:btnClick(7)).grid(row = 1, column = 0)

#Button 8

btn8 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black" , font = ('arial',20,"bold"), text = "8", command = lambda:btnClick(8)).grid(row = 1, column = 1)

#Button 9

btn9 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black" , font = ('arial',20,"bold"), text = "9", command = lambda:btnClick(9)).grid(row = 1, column = 2)

#Button +

btnAddition = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black" , font = ('arial',20,"bold"), text = "+", command = lambda:btnClick("+")).grid(row = 1, column = 3)

#-----------------------------------Second row-----------------------------------

#Button 4

btn4 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black" , font = ('arial',20,"bold"), text = "4", command = lambda:btnClick(4)).grid(row = 2, column = 0)

#Button 5

btn5 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black" , font = ('arial',20,"bold"), text = "5", command = lambda:btnClick(5)).grid(row = 2, column = 1)

#Button 6

btn6 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black" , font = ('arial',20,"bold"), text = "6", command = lambda:btnClick(6)).grid(row = 2, column = 2)

#Button -

btnSubtraction = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black" , font = ('arial',20,"bold"), text = "-", command = lambda:btnClick("-")).grid(row = 2, column = 3)

#-----------------------------------Third row-----------------------------------

#Button 1

btn1 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black" , font = ('arial',20,"bold"), text = "1", command = lambda:btnClick(1)).grid(row = 3, column = 0)

#Button 2

btn2 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black" , font = ('arial',20,"bold"), text = "2", command = lambda:btnClick(2)).grid(row = 3, column = 1)

#Button 3

btn3 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black" , font = ('arial',20,"bold"), text = "3", command = lambda:btnClick(3)).grid(row = 3, column = 2)

#Button *

btnMultiply = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black" , font = ('arial',20,"bold"), text = "*", command = lambda:btnClick("*")).grid(row = 3, column = 3)

#-----------------------------------Forth row-----------------------------------

#Button 0

btn0 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black" , font = ('arial',20,"bold"), text = "0", command = lambda:btnClick(0)).grid(row = 4, column = 0)

#Button Clear

btnClear = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black" , font = ('arial',20,"bold"), text = "C", command = btnClearDisplay()).grid(row = 4, column = 1)

#Button Equal

btnEqual = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black" , font = ('arial',20,"bold"), text = "=", command = lambda:btnEqualInput()).grid(row = 4, column = 2)

#Button Divison

btnDivison = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black" , font = ('arial',20,"bold"), text = "/", command = lambda:btnClick("/")).grid(row = 4, column = 3)


cal.mainloop()