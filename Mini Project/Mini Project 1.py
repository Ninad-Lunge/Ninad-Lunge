#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ninad
#
# Created:     04/06/2022
# Copyright:   (c) Personal 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math

#Code for Thin film Interfernce

print("Enter 1 - To find : Minimum thickness of a thin flim if it appears dark")
print("Enter 2 - To find : Minimumm thickness of a thin film if it appears bright")
print("Enter 3 - To find : Wavelength of light if thin film appears dark")
print("Enter 4 - To find : Wavelength of ligth if thin film appears bright")
print("Enter 5 - To find : Refractive Index of Film if thin film appears dark")
print("Enter 6 - To find : Refractive Index of Film if thin film appears bright")

choice = int(input("\nEnter your choice : "))

if(choice==1):
    wavelength = float(input("Enter the wavelength : ")) #500
    refractive_index = float(input("Enter the refractive index : ")) #1.5
    theta = int(input("Enter the angle of refraction : "))
    n = 1
    tmin = (n*wavelength)/(2*refractive_index*math.cos(theta)) #cos0 = 1
    print(f"The minimum thickness of the film is : {tmin}")
elif(choice==2):
    wavelength = float(input("Enter the wavelength : "))
    refractive_index = float(input("Enter the refractive index : "))
    theta = int(input("Enter the angle of refraction : "))
    n = 1
    tmin = ((2*n+1)*wavelength)/(4*refractive_index*math.cos(theta))
    print(f"The minimum thickness of the film is : {tmin}")
elif(choice==3):
    thickness = float(input("Enter the thickness of the film : "))
    refractive_index = float(input("Enter the refractive index : "))
    theta = int(input("Enter the angle of refraction : "))
    n = 1
    wavelength = (2*refractive_index*thickness*math.cos(theta))/n
    print(f"Wavelength of light is : {wavelength}")
elif(choice==4):
    thickness = float(input("Enter the thickness of the film : "))
    refractive_index = float(input("Enter the refractive index : "))
    theta = int(input("Enter the angle of refraction : "))
    n = 1
    wavelength = (4*refractive_index*thickness*math.cos(theta))/(2*n+1)
    print(f"Wavelength of light is : {wavelength}")
elif(choice==5):
    wavelength = float(input("Enter the wavelength : "))
    thickness = float(input("Enter the thickness of the film : "))
    theta = int(input("Enter the angle of refraction : "))
    n =1
    refractive_index = (n*wavelength)/(2*thickness*math.cos(theta))
    print(f"Refractive Index of film is : {refractive_index}")
elif(choice==6):
    wavelength = float(input("Enter the wavelength : "))
    thickness = float(input("Enter the thickness of the film : "))
    theta = int(input("Enter the angle of refraction : "))
    n =1
    refractive_index = ((2*n+1)*wavelength)/(4*thickness*math.cos(theta))
    print(f"Refractive Index of film is : {refractive_index}")

else:
    print("Enter a valid choice input!")


