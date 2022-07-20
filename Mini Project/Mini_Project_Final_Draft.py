import math

print("Enter a : For Thin Film Interference")
print("Enter b : For Newton's Rings")
print("Enter c : For Optical Fibre")

option = str(input("\nEnter your choice : "))

#Code for Thin film Interfernce
if(option=='a'):
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

    if(choice==2):
        wavelength = float(input("Enter the wavelength : "))
        refractive_index = float(input("Enter the refractive index : "))
        theta = int(input("Enter the angle of refraction : "))
        n = 0
        tmin = ((2*n+1)*wavelength)/(4*refractive_index*math.cos(theta))
        print(f"The minimum thickness of the film is : {tmin}")
    if(choice==3):
        thickness = float(input("Enter the thickness of the film : "))
        refractive_index = float(input("Enter the refractive index : "))
        theta = int(input("Enter the angle of refraction : "))
        n = 1
        wavelength = (2*refractive_index*thickness*math.cos(theta))/n
        print(f"Wavelength of light is : {wavelength}")
    if(choice==4):
        thickness = float(input("Enter the thickness of the film : "))
        refractive_index = float(input("Enter the refractive index : "))
        theta = int(input("Enter the angle of refraction : "))
        n = 0
        wavelength = (4*refractive_index*thickness*math.cos(theta))/(2*n+1)
        print(f"Wavelength of light is : {wavelength}")
    if(choice==5):
        wavelength = float(input("Enter the wavelength : "))
        thickness = float(input("Enter the thickness of the film : "))
        theta = int(input("Enter the angle of refraction : "))
        n =1
        refractive_index = (n*wavelength)/(2*thickness*math.cos(theta))
        print(f"Refractive Index of film is : {refractive_index}")
    if(choice==6):
        wavelength = float(input("Enter the wavelength : "))
        thickness = float(input("Enter the thickness of the film : "))
        theta = int(input("Enter the angle of refraction : "))
        n =0
        refractive_index = ((2*n+1)*wavelength)/(4*thickness*math.cos(theta))
        print(f"Refractive Index of film is : {refractive_index}")

elif(option=='b'):
    print("Enter 1 - To find : Thickness of film")
    print("Enter 2 - To find : Radius of Curvature of lens")
    print("Enter 3 - To find : Distance of film from point of contact")
    print("Enter 4 - To find : Radius of Curvature if diameter of two rings is given")
    print("Enter 5 - To find : Wavelength of light if diameter of two rings is given")

    choice = int(input("\nEnter your choice : "))
    if(choice==1):
        distance = float(input("Enter distance of film from point of contact : "))
        rad_curvature = float(input("Enter the Radius of Curvature of the Lens : "))
        thickness = (distance*distance)/2*rad_curvature
        print(f"Thickness of film is : {thickness}")
    if(choice==2):
        distance = float(input("Enter distance of film from point of contact"))
        thickness = float(input("Enter the thickness of film"))
        rad_curvature = (distance*distance)/2*thickness
        print(f"Radius of Curvature of Lens is : {rad_curvature}")
    if(choice==3):
        thickness = float(input("Enter the thickness of film"))
        rad_curvature = float(input("Enter the Radius of Curvature of the Lens : "))
        distance = math.sqrt(2*thickness*rad_curvature)
        print(f"Distance of film from point of contact is : {distance}")
    if(choice==4):
        dn = float(input("Enter the diameter of larger ring : "))
        dm = float(input("Enter the diametr of smaller ring : "))
        n = int(input("Enter the value of n : "))
        m = int(input("Enter the value of m : "))
        wavelength = float(input("Enter the wavelength of light used : "))
        rad_cu = ((dn*dn)-(dm*dm))/(4*wavelength*(n-m))
        print(f"Radius of Curvature of lens is : {rad_cu}")
    if(choice==5):
        dn = float(input("Enter the diameter of larger ring : "))
        dm = float(input("Enter the diametr of smaller ring : "))
        n = int(input("Enter the value of n : "))
        m = int(input("Enter the value of m : "))
        rad_cu = float(input("Enter the Radius of curvature of lens : "))
        rad_cu = ((dn*dn)-(dm*dm))/(4*rad_cu*(n-m))
        print(f"Wavelength of ligth used is : {wavelength}")

elif(option=='c'):
    print("Enter 1 - To find : Accetance Angle")
    print("Enter 2 - To find : Refractive Index of core")
    print("Enter 3 - To find : Refractive Index of clad")
    print("Enter 4 - To find : Numerical Apperature")
    print("Enter 5 - To find : Fractional Refractive Index")

    choice = int(input("\nEnter your choice : "))

    if(choice==1):
        core = float(input("Enter the Refractive Index of core : "))
        clad = float(input("Enter the Refractive Index of clad : "))
        acceptance_angle = math.asin(math.sqrt((core*core)-(clad*clad)))
        print(f"Acceptance angle Optical Fibre is : {math.degrees(acceptance_angle)}")
    if(choice==2):
        clad = float(input("Enter the Refractive Index of clad : "))
        acceptance_angle = float(input("Enter the Acceptance angle of Optical Fibre : "))
        a = (math.sin(acceptance_angle) ** 2) + (clad*clad)
        core = math.sqrt(a)
        print(f"The Refractive Index of Core is : {core}")
    if(choice==3):
        core = float(input("Enter the Refractive Index of core : "))
        acceptance_angle = float(input("Enter the Acceptance angle of Optical Fibre : "))
        clad = math.sqrt((core*core) - (math.sin(acceptance_angle) ** 2))
        print(f"Refractive Index of Clad is : {clad}")
    if(choice==4):
        core = float(input("Enter the Refractive Index of core : "))
        clad = float(input("Enter the Refractive Index of clad : "))
        numerical_apperature = math.sqrt((core*core)-(clad*clad))
        print(f"Numerical Apperature of Optical fibre is : {numerical_apperature}")
    if(choice==5):
        core = float(input("Enter the Refractive Index of core : "))
        clad = float(input("Enter the Refractive Index of clad : "))
        fri = (core-clad)/clad
        print(f"Fractional Refractive Index of Optical Fibre is : {fri}")
