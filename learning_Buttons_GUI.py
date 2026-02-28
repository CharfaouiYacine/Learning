from tkinter import *
fouad = Tk()
fouad.title("Son_Fouad")
count = 0
def button_clicked():  # so we are trying to create a mini project were you click the button and see how many times you clicked
    global count
    count += 1
    label.config(text=count)
image = PhotoImage(file="person.png")
button = Button(fouad,
                text="Click this button !!!",
                font=("Ink Free", 40, "bold"),
                fg="red",
                bg="light blue",
                command=button_clicked, #This line is used to call a function after clicking the button
                activebackground="pink",  # the color of bg when the button is clicked
                activeforeground="red",  # the color of fg when the button is clicked
                image = image,
                compound="bottom",
                state=ACTIVE, # use the state method ( active or disabled) to activate or to disable the button

                )
label = Label(fouad,text=count,
              font=("Arial", 40, "bold"),
              fg="green",
              )
label.pack()
button.pack()
fouad.mainloop()