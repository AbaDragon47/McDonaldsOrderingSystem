from tkinter import ttk
from tkinter import *
# LMAO WE AINT DOING TH
#create instance of the Tk class
#creates the main window of the app
root= Tk()

#name of the window
root.title("amazing person yaayy")

#width and height of the window?
root.geometry("600x400")

frame= ttk.Frame(root, padding=10) # creates the frame widget?
frame.grid()
lbl=ttk.Label(frame, text= "Hello World!").grid(column=10, row=10)#label for the window
btn=ttk.Button(frame,text="Quit", command= root.destroy).grid(column=20,row=10)
#col goes over to the right, row goes down

#in order to make button to work, we uses classes *called events in python*
#lets say you wanna make the button do something
butt= ttk.Button(frame,text="Sup Bruh").bind
root.mainloop()



