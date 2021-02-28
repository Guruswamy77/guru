import tkinter as tk
exp=""
def press(num):
    global exp
    exp=exp+str(num)
    txt1.insert(0,str(num))
def equal():
    try:
        global exp
        total=str(eval(exp))
        txt1.delete(0,tk.END)
        txt1.insert(0,total)
        exp=""
    except:
        txt1.insert("error")
        exp=""
def clear():
    global exp
    exp=""
    txt1.delete(0,tk.END)


obj=tk.Tk()
obj.title("calculator")
obj.configure(bg="navy")
obj.geometry("270x150")
lbl1=tk.Label(obj,text="enter the values")
lbl1.grid(column=1,row=1,columnspan=4)
txt1=tk.Entry(obj)
txt1.grid(column=1,row=2,columnspan=4)
btn1=tk.Button(obj,text="9",fg="black",bg="white",command=lambda:press(9))
btn1.grid(column=0,row=3)
btn2=tk.Button(obj,text="8",fg="black",bg="white",command=lambda:press(8))
btn2.grid(column=1,row=3)
btn3=tk.Button(obj,text="7",fg="black",bg="white",command=lambda:press(7))
btn3.grid(column=2,row=3)

btn4=tk.Button(obj,text="+",fg="black",bg="white",command=lambda:press("+"))
btn4.grid(column=3,row=3)

btn5=tk.Button(obj,text="6",fg="black",bg="white",command=lambda:press(6))
btn5.grid(column=0,row=4)
btn6=tk.Button(obj,text="5",fg="black",bg="white",command=lambda:press(5))
btn6.grid(column=1,row=4)
btn7=tk.Button(obj,text="4",fg="black",bg="white",command=lambda:press(4))
btn7.grid(column=2,row=4)

btn8=tk.Button(obj,text="-",fg="black",bg="white",command=lambda:press("-"))
btn8.grid(column=3,row=4)

btn9=tk.Button(obj,text="3",fg="black",bg="white",command=lambda:press(3))
btn9.grid(column=0,row=5)
btn10=tk.Button(obj,text="2",fg="black",bg="white",command=lambda:press(2))
btn10.grid(column=1,row=5)
btn11=tk.Button(obj,text="1",fg="black",bg="white",command=lambda:press(1))
btn11.grid(column=2,row=5)

btn12=tk.Button(obj,text="*",fg="black",bg="white",command=lambda:press("*"))
btn12.grid(column=3,row=5)

btn13=tk.Button(obj,text="clear",fg="black",bg="red",command=lambda:clear())
btn13.grid(column=0,row=6)
btn14=tk.Button(obj,text="0",fg="black",bg="white",command=lambda:press(0))
btn14.grid(column=2,row=6)
btn15=tk.Button(obj,text="/",fg="black",bg="white",command=lambda:press("/"))
btn15.grid(column=3,row=6)
btn16=tk.Button(obj,text="  =  ",fg="black",bg="light green",command=lambda:equal())
btn16.grid(column=1,row=6)







