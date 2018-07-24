# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:25:49 2018

@author: sumerac
"""
#import tkinter.messagebox
import tkinter
from tkinter import messagebox

Conversion_box = tkinter.Tk()
top_frame = tkinter.Frame(Conversion_box)
bottom_frame = tkinter.Frame(Conversion_box)

tkinter.Label(top_frame, text = 'Enter a distance in Kilometers: ').pack(side = 'left')
km_entry = tkinter.Entry(top_frame, width = 10); km_entry.pack(side = 'left')

def convert():
    km = float(km_entry.get())
    miles = km * 0.6214
    tkinter.messagebox.showinfo('Result', '%.2f kilometers is equal to %.2f miles.' % (km, miles) )

tkinter.Button(bottom_frame, text = 'Convert', bg="yellow", fg="black",command = convert).pack(side = 'left')
tkinter.Button(bottom_frame, text = 'Quit', bg="yellow", fg="black", command = Conversion_box.destroy).pack(side = 'left')

top_frame.pack()
bottom_frame.pack()

tkinter.mainloop()

