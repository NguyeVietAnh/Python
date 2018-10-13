'''
Oct 12,  2018
Recipe:  B04829_01_01
@author: Kai
'''
import tkinter as tk
from tkinter import ttk 
win = tk.Tk()
win.title ("Motor Driver")
#win.resizable(0,0)                   # Make user can't resize the windows

#Modify adding a Label
ttk.Label(win, text = "Speed of The Motor").grid (column =0, row = 0)

#Button Click Event Function
def clickMe ():
    action.configure(text = "** I have been Clicked! **")
    aLabel.configure (foreground = 'red')
    aLabel.configure (text = 'A Red Label')
    
# Adding a Button
action = ttk.Button (win, text ="Click Me!", command = clickMe)
action.grid(column = 1, row =0)

win.mainloop()
