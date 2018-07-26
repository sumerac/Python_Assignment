# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:26:42 2018

@author: sumerac
"""
#Source: https://stackoverflow.com/questions/37598991/how-
#to-plot-two-specific-columns-from-a-csv-file-in-python



#import numpy as np
import csv
import math
#from math import sqrt
#import tkinter
#from tkinter import messagebox

#from tkinter import messagebox
# 
#import tkinter as tk
#master = tk.Tk()
#whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
##messagebox.showinfo("Title", "a Tk MessageBox")
#
#msg = tk.Message(master, text = whatever_you_do)
#msg.config(bg='lightblue', font=('times', 16, 'bold'))
#msg.pack()
#tk.mainloop()

#Speed_warning = tkinter.Tk()
#top_frame = tkinter.Frame(Speed_warning)
#bottom_frame = tkinter.Frame(Speed_warning)
#tkMessageBox.showinfo(title="Over Speed", message="Please Slow down!
#driving_speed = np.genfromtxt('Sensor_record_7_24_18_AndroSensor.csv', delimiter=',')

def getColumn(filename, column):
    results = csv.reader(open(filename), dialect='excel')
    return [result[column] for result in results]

#Accelerometer data in meters per second squared in x, y, z directions and time since start
ACC_X = getColumn('Speed_data.csv', 0)
ACC_Y = getColumn('Speed_data.csv', 1)
ACC_Z = getColumn('Speed_data.csv', 2)
TIME = getColumn('Speed_data.csv', 3)
SPEED = getColumn('Speed_data.csv', 4)
#print(SPEED)

speed_mph = []
for row in range(1,len(SPEED)):
    speed_mph.append(float(SPEED[row])*0.6214)
    print(speed_mph)

def speedLimit = 46
if speed_mph > speedLimit:
    
for row in speed_mph:
    if row > speedLimit:
        speedAboveLimit += 1
        
#import tkMessageBox
")



    

    
# warning for speed over 46mph
    

#vx = []
#for row in range(1,len(ACC_X)):
#    vx.append(float(ACC_X[row])*float(TIME[row]))
##print(vx)
#
#vy = []
#for row in range(1,len(ACC_Y)):
#    vy.append(float(ACC_Y[row])*float(TIME[row]))
#    print(vy)



#vx += ax * dt;     |v|=sqrt(vx**2+vy**2+vz**2)  a1 = sqrt(x*x + y*y + z*z)

#data_arry=np.array(fdata)

#vx = ACC_X=[:,1]*TIME[:,4] 
#print ("ACC_X")


#def vx()
#def qmean(num):
#	return sqrt(sum(n*n for n in num)/len(num))
