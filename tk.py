import PySimpleGUI as sg
from StockScraper import *

from tkinter import *

def clicked():
    #pulls up info
    gosearch(txt.get())
    lbl.configure(text = txt.get())
    currentP.configure(text = price)

master = Tk()
currentP = Label(master, text='')
OpenP = Label(master,text='')
DayHigh = Label(master,text='')
DayLow = Label(master,text='')
lbl = Label(master, text='Hello')
lbl.grid(column=2,row=0)
txt = Entry(master, width = 10)
txt.grid(column=1, row=0)

btn = Button(master, text='Search', command=clicked)
btn.grid(column=1, row=1)

master.mainloop()

