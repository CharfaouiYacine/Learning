from tkinter import *
fouad = Tk()
#Label : ar area widget that holds text or/and an image  within a window
photo = PhotoImage(file="person.png")
label = Label(fouad,
              text="I am The GOAT:)", # The text we want to write
              font=("Arial", 40, "bold"), # The font and the size and the type
              fg="white", # The color of the text either with name of hex code
              bg="#000000", # the background color
              relief=RAISED, # THis is the border type
              bd = 20, # The size of the border
              padx = 10, pady = 10, # padding between the text and the border using x and y
              image = photo,
              compound="bottom", # Use this to know where to put the image according to the text


              )
#label.place(x=0, y=0) add the label to the window with special coordinates
label.pack() #adds the label to the window
fouad.mainloop()