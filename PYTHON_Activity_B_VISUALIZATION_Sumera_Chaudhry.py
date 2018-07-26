# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:14:50 2018

@author: sumerac
"""

import pandas as panda
import matplotlib.pyplot as plt

"""READING DATA FROM CSV FILE"""
df = panda.read_csv('Sensor_data.csv')
ACC_X = df['ACCELEROMETER X (m/s^2)']
ACC_Y = df['ACCELEROMETER Y (m/s^2)']
ACC_Z = df['ACCELEROMETER Z (m/s^2)']
SPEED = df['LOCATION Speed (Kmh)']
TIME = df['Time in ms']

"""PLOTTING ACCELEROMETER DATA"""
plt.figure(1)
plt.grid(b=True, which='both', color='y', linestyle='-')
plt.plot(TIME/1000, ACC_X, 'b')
plt.plot(TIME/1000, ACC_Y, 'g')
plt.plot(TIME/1000, ACC_Z, 'r')
plt.xlabel('Xaxis --> Time_ms')
plt.ylabel('Yaxis --> Accelerometer m/s^2')
plt.title('Sensor data for Accelerometer Vs Time')
legend = plt.legend(loc='best', shadow=True, fontsize='medium')
legend.get_frame().set_facecolor('#99ffdd')
plt.show()

"""PLOTTING ACCERELOMETER DATA IN SUBPLOTS"""
f, axes = plt.subplots(3, 1)
"""SUBPLOT 1"""
axes[0].plot(TIME/1000, ACC_X, 'g')
axes[0].set_ylabel('Accelerometer X m/s^2')
axes[0].set_title('Accelerometer XYZ(m/s^2) vs Time')
axes[0].grid(b=True, which='both', color='r', linestyle='-')
axes[0].legend(loc='best', shadow=True, fontsize='small')\
               .get_frame().set_facecolor('#99ffdd')
"""SUBPLOT 2"""
axes[1].plot(TIME/1000, ACC_Y, 'r')
axes[1].set_ylabel('Accelerometer Y m/s^2')
axes[1].grid(b=True, which='both', color='b', linestyle='-')
axes[1].legend(loc='best', shadow=True, fontsize='small')\
               .get_frame().set_facecolor('#ff99e6')
"""SUBPLOT 3"""
axes[2].plot(TIME/1000, ACC_Z, 'k')
axes[2].set_xlabel('Time (secs)')
axes[2].set_ylabel('Accelerometer Z m/s^2')
axes[2].grid(b=True, which='both', color='g', linestyle='-')
axes[2].legend(loc='best', shadow=True, fontsize='small')\
               .get_frame().set_facecolor('#ffff4d')

"""PLOTTING SPEED VS TIME"""
plt.figure()
plt.grid(b=True, which='both', color='y', linestyle='-')
plt.plot(TIME/1000, SPEED, 'm')
plt.xlabel('Xaxis --> Time_secs')
plt.ylabel('Yaxis --> Speed mph')
plt.title('Sensor location Speed Vs Time')
legend = plt.legend(loc='best', shadow=True, fontsize='medium')
legend.get_frame().set_facecolor('#99ffdd')
plt.show()

SPEED_MPH = SPEED*.621371
plt.figure()
plt.grid(b=True, which='both', color='b', linestyle='-')
plt.plot(TIME/1000, SPEED_MPH, 'r')
plt.xlabel('Xaxis --> Time_secs')
plt.ylabel('Yaxis --> Speed mph')
plt.title('Sensor location Speed (MPH) Vs Time (sec)')
legend = plt.legend(loc='best', shadow=True, fontsize='medium')
legend.get_frame().set_facecolor('#99ffdd')
plt.show()

"""CHECKING FOR ANY OVERSPEEDING AND PRINTING WARNING ALERT"""
speed_mph = [0]
for row in range(1, len(SPEED)):
    speed_mph.append(float(SPEED[row])*0.6214)
    if (speed_mph[row] > 42.6):
        speed_mph = speed_mph
        print("WARNING: You're OVERSPEEDING. Kindly, SLOW DOWN")
