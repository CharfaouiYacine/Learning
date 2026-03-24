from tkinter import *
import tkinter as tk

"""Section of functions of the calculator"""
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        print("Can't divide by zero")
        return None
    else:
        return a / b
def floordiv(a, b):
    if b == 0:
        print("Can't divide by zero")
        return None
    else:
        return a // b
def mod(a, b):
    return a % b
def pow(a, b):
    return a ** b

def history():
    history_list.delete(0, END)
    if not hist:
        history_list.insert(0,"No history yet")
        return
    else:
        for calc in hist:
            history_list.insert(0, calc)

def but_clicked(character):
    if result_text.get()=="0":
        if character in ["+","-","*","/","f","^","%"]:
            result_text.set(f"{result_text.get()}")
        else:
            result_text.set(f"{character}")
    elif character in ["+","-","*","/","f","^","%"]:
        if result_text.get()[-1] in ["+","-","*","/","f","^","%"]:
            result_text.set(f"{result_text.get()[:-1]}{character}")
        else:
            result_text.set(f"{result_text.get()}{character}")
    else:
        result_text.set(f"{result_text.get()}{character}")

def equal(equation):
    arr = []
    number = str()
    if len(equation) <= 1:
        result_text.set(f"{equation.get()}")
        return

    else:
        for i in equation:
            if i in ["+","-","*","/","f","^","%"]:
                arr.append(float(number))
                if not(i==equation[-1]):
                    arr.append(i)
                number = str()
            else:
                number=number+i
        if not (len(number) == 0):
            arr.append(float(number))

        while len(arr) > 1:
            for i in range(len(arr)):
                if arr[i] == "^":
                    f_result = operations[arr[i]](arr[i-1],arr[i+1])
                    arr[i-1:i+2] = [f_result]
                    break

            for i in range(len(arr)):
                if arr[i] in ["*","/","f","%"]:
                    f_result = operations[arr[i]](arr[i-1],arr[i+1])
                    arr[i-1:i+2]=[f_result]
                    break

            for i in range(len(arr)):
                if arr[i] in ["+","-"]:
                    f_result = operations[arr[i]](arr[i-1],arr[i+1])
                    arr[i-1:i+2]=[f_result]
                    break


            if any(i in ["+","-","*","/","f","^","%"] for i in arr):
                continue
            else:
                break
        if arr[0] % 1 ==0:
            result_text.set(f"{int(arr[0])}")
            hist.append(f"{equation}={int(arr[0])}")
            history_list.insert(0, f"{equation}={int(arr[0])}")
        else:
            result_text.set(f"{arr[0]}")
            hist.append(f"{equation}={arr[0]}")
            history_list.insert(0,f"{equation}={arr[0]}")

def clear():
    result_text.set("0")

def clear_hist():
    history_list.delete(0, END)

def backspace():
    if result_text.get() == "0":
        return
    elif len(result_text.get()) == 1:
        result_text.set("0")
    else:
        result_text.set(result_text.get()[0:-1])
"""-----------------------------------------------------------------------------"""
operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/":div,
        "f": floordiv,
        "^": pow,
        "%": mod
    }
ans = None
hist = []

"""------The UI part of the calculator------"""
calculator = Tk()
calculator.title("Calculator")
calculator.configure(background="#1e1e2f")
calc_image = PhotoImage(file="calculator_9597350.png")
result_text = tk.StringVar()
result_text.set("0")

top_frame = Frame(calculator)
hist_frame = Frame(top_frame)
history_text = Label(hist_frame,text="History",font=("Arial",15,"bold"),bg="#363659",fg="white",width=31,height=3)
history_text.pack(side="left")
but_chist= Button(hist_frame,text="🗑",font=("Arial",15),bg="#363659",fg="#ffffff",width=11,height=3,command=lambda :clear_hist())
but_chist.pack(side="left")
hist_frame.pack(side="top")
history_list = Listbox(top_frame,bg="#363659",fg="white",font=("Arial",22,"bold"),width=32, height=20)
history_list.pack(side="left")
top_frame.pack(side="right")

whole_frame = Frame(calculator,bg="#39397D")
sixth_row = Frame(whole_frame,bg="#39397D")
result = Label(sixth_row,textvariable=result_text,font=("Arial",22,"bold"),bg="#2d2d44",fg="#ffffff",width=25,height=2-3)
result.pack(side="left",padx=7,pady=7)
but_bs= Button(sixth_row,text="⌫",font=("Arial",12,"bold"),bg="#d32f2f",fg="#ffffff",width=11,height=2,command=lambda :backspace())
but_bs.pack(side="left",padx=5,pady=5)
sixth_row.pack(pady=10)

oper_frame = Frame(whole_frame,bg="#39397D")
fifth_row = Frame(oper_frame,bg="#39397D")
but_div = Button(fifth_row,text="/",font=("Arial",12,"bold"),bg="#3b4261",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("/"))
but_div.pack(side="left",padx=5,pady=5)
but_fdiv = Button(fifth_row,text="//",font=("Arial",12,"bold"),bg="#3b4261",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("f"))
but_fdiv.pack(side="left",padx=5,pady=5)
but_pow = Button(fifth_row,text="^",font=("Arial",12,"bold"),bg="#3b4261",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("^"))
but_pow.pack(side="left",padx=5,pady=5)
but_mod = Button(fifth_row,text="%",font=("Arial",12,"bold"),bg="#3b4261",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("%"))
but_mod.pack(side="left",padx=5,pady=5)
but_his = Button(fifth_row,text="History",font=("Arial",12,"bold"),bg="#3b4261",fg="#ffffff",width=10,height=2,command=lambda :history())
but_his.pack(side="left",padx=5,pady=5)
fifth_row.pack(pady=4)

fourth_row = Frame(oper_frame,bg="#39397D")
but_7 = Button(fourth_row,text="7",font=("Arial",12,"bold"),bg="#3a3a5a",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("7"))
but_7.pack(side="left",padx=5,pady=5)
but_8 = Button(fourth_row,text="8",font=("Arial",12,"bold"),bg="#3a3a5a",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("8"))
but_8.pack(side="left",padx=5,pady=5)
but_9 = Button(fourth_row,text="9",font=("Arial",12,"bold"),bg="#3a3a5a",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("9"))
but_9.pack(side="left",padx=5,pady=5)
but_mul = Button(fourth_row,text="*",font=("Arial",12,"bold"),bg="#3b4261",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("*"))
but_mul.pack(side="left",padx=5,pady=5)
fourth_row.pack(pady=4)

third_row = Frame(oper_frame,bg="#39397D")
but_4 = Button(third_row,text="4",font=("Arial",12,"bold"),bg="#3a3a5a",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("4"))
but_4.pack(side="left",padx=5,pady=5)
but_5 = Button(third_row,text="5",font=("Arial",12,"bold"),bg="#3a3a5a",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("5"))
but_5.pack(side="left",padx=5,pady=5)
but_6 = Button(third_row,text="6",font=("Arial",12,"bold"),bg="#3a3a5a",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("6"))
but_6.pack(side="left",padx=5,pady=5)
but_minus = Button(third_row,text="-",font=("Arial",12,"bold"),bg="#3b4261",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("-"))
but_minus.pack(side="left",padx=5,pady=5)
third_row.pack(pady=4)

second_row = Frame(oper_frame,bg="#39397D")
but_1 = Button(second_row,text="1",font=("Arial",12,"bold"),bg="#3a3a5a",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("1"))
but_1.pack(side="left",padx=5,pady=5)
but_2 = Button(second_row,text="2",font=("Arial",12,"bold"),bg="#3a3a5a",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("2"))
but_2.pack(side="left",padx=5,pady=5)
but_3 = Button(second_row,text="3",font=("Arial",12,"bold"),bg="#3a3a5a",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("3"))
but_3.pack(side="left",padx=5,pady=5)
but_plus = Button(second_row,text="+",font=("Arial",12,"bold"),bg="#3b4261",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("+"))
but_plus.pack(side="left",padx=5,pady=5)
second_row.pack(pady=4)

first_row = Frame(oper_frame,bg="#39397D")
but_c= Button(first_row,text="C",font=("Arial",12,"bold"),bg="#d32f2f",fg="#ffffff",width=11,height=2,command=lambda :clear())
but_c.pack(side="left",padx=5,pady=5)
but_0= Button(first_row,text="0",font=("Arial",12,"bold"),bg="#3a3a5a",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("0"))
but_0.pack(side="left",padx=5,pady=5)
but_point =Button(first_row,text=".",font=("Arial",12,"bold"),bg="#3b4261",fg="#ffffff",width=10,height=2,command=lambda :but_clicked("."))
but_point.pack(side="left",padx=5,pady=5)
but_equal = Button(first_row,text="=",font=("Arial",12,"bold"),bg="#00c853",fg="#ffffff",width=12,height=2,command=lambda :equal(result_text.get()))
but_equal.pack(side="left",padx=5,pady=5)
first_row.pack(pady=4)

oper_frame.pack(side="right")
whole_frame.pack(side="right")
calculator.iconphoto(True, calc_image)
calculator.mainloop()

"""-----------------------------------------------"""

"""  
------------This the code that i used for  the terminal version -------------
def get_number(prompt,ans):
    while True:
        try:
            num = input(prompt).strip().lower()
            if num == "ans":
                if ans is None:
                    print("no ans yet enter a number please ")
                    continue
                else:
                    num = ans
            else:
                num = float(num)
            return num
        except ValueError:
            print("Can't use alphabets or special characters!!")


while True:
    print("Operators: + , - , * , / , // , % , **, h | Type exit to quit")
    operator = input("Please enter your operator/command: ").strip().lower()
    while operator not in ["+", "-", "*", "/","**","%","//","exit","h"]:
        operator = input("Please enter your operator: ").strip().lower()
    if operator == "exit":
        break
    elif operator == "h":
        history()
        continue
    num1 = get_number("Enter first number: ",ans)
    num2 = get_number("Enter second number: ",ans)
    result = operations[operator](num1, num2)
    if result is not None:
        print(f"{num1} {operator} {num2} = {result}")
        hist.append(f"{num1} {operator} {num2} = {result}")
        ans = result
-------------------------------------------------------------------------------
"""

"""
First of all Alhamdulilah , today i was able to finish a mini project of calculator with some simple
operations 
"""