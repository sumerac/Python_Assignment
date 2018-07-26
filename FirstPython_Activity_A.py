# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:25:49 2018

@author: sumerac
"""
# SOURCE: https://stackoverflow.com/questions/41886219/conversion-of-kilometers
# -to-miles
# Program only works with integers

KM_TO_MILES = 0.621371


def show_km2mi(Distance):

    miles = Distance * KM_TO_MILES
    print('{} kilometers converts to {} miles'.format(Distance, miles))


def main():
    RESET = True
    while (RESET):
        Distance = input(
                "Please enter the distance in kilometers that you wish"
                " to convert in miles: ")
        while (not Distance.isdigit()):
            print(Distance)
            Distance = input(
                "Please enter the distance in kilometers that you wish"
                " to convert in miles: ")

        Distance = float(Distance)
        print(Distance)
        show_km2mi(Distance)
        convertagain = input("Do you wish to convert more numbers: y/n?")
        while (not(convertagain.upper() == "Y" or
               convertagain.upper() == "N")):
            print(convertagain)
            convertagain = input("Do you wish to convert more numbers: y/n?")
        print(convertagain)
        if (convertagain == "n" or convertagain == "N"):
            RESET = False
main()
