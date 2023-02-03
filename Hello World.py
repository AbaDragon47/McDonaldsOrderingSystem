from tkinter import ttk
from tkinter import *

#create instance of the Tk class
#creates the main window of the app
root= Tk()
frame= ttk.Frame(root, padding=10) # creates the frame widget?
frame.grid()
lbl=ttk.Label(frame, text= "Hello World!").grid(column=0, row=0)#label for the window
btn=ttk.Button(frame,text="Quit", command= root.destroy).grid(column=1,row=0)
root.mainloop()



