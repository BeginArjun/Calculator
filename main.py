import os
from src import window
from cgitb import text
from tkinter import *
from tkinter import font

root=window.window()

# Get Relative PATH
def rcpath(rel_path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)),rel_path)
# Adding Icon

LOGO_PATH='images\calculator-icon.ico'
root.iconbitmap(rcpath(LOGO_PATH))

# Add Two Numbers
def btnClick(number):
    curr=inputField.get()
    inputField.delete(0,END)
    inputField.insert(0,str(curr)+str(number))


# Clear The Screen
def clear():
    inputField.delete(0,END)
    global textExpression
    textExpression=' '
    prevLabel=Label(frameRes,text=textExpression,font=('Arial 10'),bg='white')
    prevLabel.grid(row=0,column=1)

# Adding Function
def add():
    curr=inputField.get()
    global f_num
    global math
    global textExpression
    inputField.delete(0,END)
    textExpression=str(curr)+"+"
    prevLabel=Label(frameRes,text=textExpression,font=('Arial 10'),bg='white')
    prevLabel.grid(row=0,column=1)
    if curr=='':
        inputField.insert(0,"Please Input Number")
        return
    math="addition"
    f_num=int(curr)

# Subtract
def subtract():
    curr=inputField.get()
    global f_num
    global math
    global textExpression
    inputField.delete(0,END)
    textExpression=str(curr)+"-"
    prevLabel=Label(frameRes,text=textExpression,font=('Arial 10'),bg='white')
    prevLabel.grid(row=0,column=1)
    if curr=='':
        inputField.insert(0,"Please Input Number")
        return
    math="subtraction"
    f_num=int(curr)

# Multiply
def multiply():
    curr=inputField.get()
    global f_num
    global math
    global textExpression
    inputField.delete(0,END)
    textExpression=str(curr)+"x"
    prevLabel=Label(frameRes,text=textExpression,font=('Arial 10'),bg='white')
    prevLabel.grid(row=0,column=1)
    if curr=='':
        inputField.insert(0,"Please Input Number")
        return
    math="multiply"
    f_num=int(curr)

# Divide
def divide():
    curr=inputField.get()
    global f_num
    global math
    global textExpression
    inputField.delete(0,END)
    textExpression=str(curr)+"/"
    prevLabel=Label(frameRes,text=textExpression,font=('Arial 10'),bg='white')
    prevLabel.grid(row=0,column=1)
    if curr=='':
        inputField.insert(0,"Please Input Number")
        return
    math="divide"
    f_num=int(curr)


# Display Result

def display():
    curr=int(inputField.get())
    inputField.delete(0,END)
    res=int()
    global textExpression 
    textExpression+= str(curr)+"="
    prevLabel=Label(frameRes,text=textExpression,font=('Arial 10'),bg='white')
    prevLabel.grid(row=0,column=1)
    if math=="addition":
        res=curr+f_num
    elif math=="subtraction":
        res=f_num-curr
    elif math=="multiply":
        res=f_num*curr
    elif math=="divide":
        res=f_num/curr
    inputField.insert(0,res)


if __name__=="__main__":
    # Frame for Result
    frameRes=Frame(root,bg='white')
    frameRes.grid(row=0,column=0)
    # Entry or Display
    inputField=Entry(frameRes,width=35,bg='white',justify='right',font=('Arial 20'))
    inputField.grid(row=1,column=0,columnspan=1,padx=30,pady=20)

    # Frame for Buttons
    frameDigits=Frame(root)
    frameDigits.grid(row=1,column=0)
    # Digit Buttons
    button0=Button(frameDigits,text="0",padx=40,pady=20,command=lambda: btnClick(0))
    button1=Button(frameDigits,text="1",padx=40,pady=20,command=lambda: btnClick(1))
    button2=Button(frameDigits,text="2",padx=40,pady=20,command=lambda: btnClick(2))
    button3=Button(frameDigits,text="3",padx=40,pady=20,command=lambda: btnClick(3))
    button4=Button(frameDigits,text="4",padx=40,pady=20,command=lambda: btnClick(4))
    button5=Button(frameDigits,text="5",padx=40,pady=20,command=lambda: btnClick(5))
    button6=Button(frameDigits,text="6",padx=40,pady=20,command=lambda: btnClick(6))
    button7=Button(frameDigits,text="7",padx=40,pady=20,command=lambda: btnClick(7))
    button8=Button(frameDigits,text="8",padx=40,pady=20,command=lambda: btnClick(8))
    button9=Button(frameDigits,text="9",padx=40,pady=20,command=lambda: btnClick(9))

    # Packing the digit buttons
    button1.grid(row=3,column=0)
    button2.grid(row=3,column=1)
    button3.grid(row=3,column=2)
    button4.grid(row=2,column=0)
    button5.grid(row=2,column=1)
    button6.grid(row=2,column=2)
    button7.grid(row=1,column=0)
    button8.grid(row=1,column=1)
    button9.grid(row=1,column=2)
    button0.grid(row=4,column=0)

    # Symbols & Function Buttons
    addButton=Button(frameDigits,text="+",padx=40,pady=20,command=add)
    subtractButton=Button(frameDigits,text="-",padx=40,pady=20,command=subtract)
    multiplyButton=Button(frameDigits,text="X",padx=40,pady=20,command=multiply)
    divideButton=Button(frameDigits,text="/",padx=40,pady=20,command=divide)
    equalButton=Button(frameDigits,text="=",padx=40,pady=20,fg='white',bg='blue',command=display)
    clsButton=Button(frameDigits,text="C",padx=40,pady=20,command=clear)

    # Packing Buttons
    clsButton.grid(row=1,column=3,columnspan=2)
    addButton.grid(row=3,column=3)
    subtractButton.grid(row=2,column=3)
    multiplyButton.grid(row=4,column=3)
    divideButton.grid(row=4,column=2)
    equalButton.grid(row=4,column=1)

    # Main Loop
    root.mainloop()
