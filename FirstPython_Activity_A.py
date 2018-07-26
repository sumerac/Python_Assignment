# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:25:49 2018

@author: sumerac
"""
# SOURCE: https://stackoverflow.com/questions/41886219/conversion-of-kilometers
# -to-miles

KM_TO_MILES = 0.621371

def show_km2mi(Distance):
    miles = Distance * KM_TO_MILES
    print('{} kilometers converts to {} miles'.format(Distance, miles))

def main():
    Distance = float(input
                     ("Please enter the distance in kilometers that you wish 
                      to convert in miles: "))
    show_km2mi(Distance)

main()
