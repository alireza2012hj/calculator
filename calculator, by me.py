import colorama
from colorama import init, Fore, Style
import sys
import time
import math

# # import turtle
# # String = "Ali"
# # int = 32767
# # float = 69.420
# # boolean_true_false = True
# # print()

# age = input("Enter your Age you son of a pickle: ")
# name = input("Enter your name you son of a pickle: ")
# weight = 69.5
# is_brainrot = True

# age = int(input("Please Enter your age: "))  # Convert age to an integer
# name = input("Please Enter Your Name: ")
# print("---------------------------------")
# print("---------------------------------")
# print("This is your real age: " + str(age - 5))  # Subtract 5 from age and convert back to string
# print("This is your name: " + name)
# print("and this is Your Dad: ")

# messege = "Roham Academy"

# print(len(messege))
# print(messege.upper())
# print(messege.lower())
# print(messege.title())
# print(messege.replace("a", "o"))

# x = 6
# y = 7

# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x%y)
# print(x**y)

# Initialize Colorama (for terminal color support)
init()

def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def permutation(n, r):
    return factorial(n) // factorial(n - r)

def permutation_with_repetition(n, r):
    return n ** r  # n raised to the power of r

def tiem():
    time.sleep(1)

def dots():
    print(".", flush=True, end='')
    tiem()
    print(".", flush=True, end='')

def animation():
    print("Calculating"+".", flush=True, end='')
    tiem()
    print(".", flush=True, end='')
    tiem()
    print(".\n", flush=True, end='')
    tiem()

pi = 3.14159




def calculator():
    print(Fore.WHITE + "Welcome to the ULTIMATE HYPER CALCULATOR PRO MAX PLUS PLUS+++++++++ !!!!!!!!!!!1!11!")
    print(Fore.CYAN + "------------------------------------")

    # Present menu options
    print(Fore.YELLOW + "Choose what you want to calculate:\n")

    print(Fore.GREEN + "1." + Fore.WHITE + " Area and Primeter of a Circle")

    print(Fore.GREEN + "2." + Fore.WHITE + " Area and Primeter of a Rectangle")

    print(Fore.GREEN + "3." + Fore.WHITE + " Area and Primeter of a Rhombus")
    
    print(Fore.GREEN + "4." + Fore.WHITE + " Combinations")
    
    print(Fore.GREEN + "5." + Fore.WHITE + " Permutations")
    
    print(Fore.GREEN + "6." + Fore.WHITE + " Permutation With Reputition")
    
    print(Fore.GREEN + "7." + Fore.WHITE + " Triangle")
    
    print(Fore.GREEN + "8." + Fore.WHITE + " Square")
    
    print(Fore.GREEN + "9." + Fore.WHITE + " Trapezoid")
    
    print(Fore.GREEN + "10." + Fore.WHITE + " Factorial")
    
    print(Fore.GREEN + "11." + Fore.WHITE + " 3D shapes")

    print(Fore.CYAN + "------------------------------------")

    # Get user choice
    choice = input(Fore.WHITE + "Enter your choice (1, 2, 3, etc.): " + Fore.YELLOW)

    # Handle user's choice
    if choice == "1":
        # Circle Area Calculation

        diameter = int(input(Fore.WHITE + "Enter the diameter of the circle: " + Fore.MAGENTA))
        radius = diameter / 2


        area_circle = (radius ** 2) * pi
        perimeter_circle = diameter * pi

        animation()

        print("-------------------------------------------------------------------" + Fore.WHITE + "\nThe " + Fore.GREEN + "area" + Fore.WHITE + " of the circle is: " + Fore.BLUE + str(area_circle))
        print("-------------------------------------------------------------------" + Fore.WHITE + "\nThe " + Fore.GREEN + "perimeter" + Fore.WHITE + " of the circle is: " + Fore.BLUE + str(perimeter_circle) + Fore.WHITE)

    elif choice == "2":
        # Rectangle Area Calculation
        print(Fore.WHITE + "\nYou chose to calculate the area of a Rectangle.")
        length = int(input(Fore.WHITE + "Enter the length of the rectangle: " + Fore.MAGENTA))
        width = int(input(Fore.WHITE + "Enter the width of the rectangle: " + Fore.MAGENTA))

        animation()     #print(Fore.WHITE + "\nCalculating the" + Fore.GREEN + " area " + Fore.WHITE + "of a" + Fore.BLUE + " Rectangle" + Fore.WHITE + ", Please be patient...")

        area_rectangle = length * width
        perimeter_rectangle = 2 * (length + width)

        print("-------------------------------------------------------------------" + Fore.WHITE + "\nThe " + Fore.GREEN + "area" + Fore.WHITE + " of the rectangle is: " + Fore.BLUE + str(area_rectangle))
        print("-------------------------------------------------------------------" + Fore.WHITE + "\nThe " + Fore.GREEN + "perimeter" + Fore.WHITE + " of the rectangle is: " + Fore.BLUE + str(perimeter_rectangle) + Fore.WHITE)

    elif choice == "3":
        # Rhombus Calculation
        Pdiagonal = int(input(Fore.WHITE + "Please enter the" + Fore.YELLOW + " Smaller Diagonal: " + Fore.MAGENTA))
        Qdiagonal = int(input(Fore.WHITE + "Please enter the" + Fore.YELLOW + " Bigger Diagonal: " + Fore.MAGENTA))
        side_rhombus = int(input(Fore.WHITE + "Please enter the" + Fore.YELLOW + " Side " + Fore.WHITE + "of the Rhombus: " + Fore.MAGENTA))

        animation()

        area_rhombus = int((Pdiagonal * Qdiagonal)) / 2
        perimeter_rhombus = int(side_rhombus * 4)

        print(Fore.WHITE + "the" + Fore.GREEN + " area " + Fore.WHITE + "of the Rhombus is: " + Fore.RED + str(area_rhombus))
        print(Fore.WHITE + "the" + Fore.GREEN + " perimeter " + Fore.WHITE + "of the Rhombus is: " + Fore.RED + str(perimeter_rhombus))

    elif choice == "4":
        # Combination Calculation
        n = int(input(Fore.WHITE + "Enter the number of " + Fore.YELLOW + "Items: " + Fore.MAGENTA))
        r = int(input(Fore.WHITE + "Enter the number of " + Fore.YELLOW + "Slots: " + Fore.MAGENTA))

        animation()

        combination_ = combination(n, r)

        if r > n:
            print(Fore.RED + "Slots cannot be more than Items")
        else:
            print(Fore.WHITE + "There is " + Fore.GREEN + str(combination_) + Fore.WHITE + " different " + Fore.RED + "combinations " + Fore.WHITE + "of " + Fore.MAGENTA + str(n) + " Items And " + str(r) + " Slots!")

    elif choice == "5":
        # Permutation Calculation
        N = int(input(Fore.WHITE + "Enter the number of " + Fore.YELLOW + "Items: " + Fore.MAGENTA))
        R = int(input(Fore.WHITE + "Enter the number of " + Fore.YELLOW + "Slots: " + Fore.MAGENTA))

        animation()

        permutation_ = permutation(N, R)

        if R > N:
            print(Fore.RED + "Slots cannot be more than Items")
        else:
            print(Fore.WHITE + "There is " + Fore.GREEN + str(permutation_) + Fore.WHITE + " different " + Fore.RED + "Permutations " + Fore.WHITE + "of " + Fore.MAGENTA + str(N) + " Items And " + str(R) + " Slots!")

    elif choice == "6":
        nn = int(input(Fore.WHITE + "Enter the number of " + Fore.YELLOW + "Items: " + Fore.MAGENTA))
        rr = int(input(Fore.WHITE + "Enter the number of " + Fore.YELLOW + "Slots: " + Fore.MAGENTA))

        animation()

        permutation_with_reputition = permutation_with_repetition(nn, rr)

        if rr > nn:
            print(Fore.RED + "Slots cannot be more than Items")
        else:
            print(Fore.WHITE + "There is " + Fore.YELLOW + str(permutation_with_reputition) + Fore.WHITE + " different " + Fore.RED + "Permutation With Repitition " + Fore.WHITE + "of " + Fore.MAGENTA + str(nn) + " Items And " + str(rr) + " Slots!")

    elif choice == "7":
        base_triangle = int(input(Fore.WHITE+"Enter the " + Fore.GREEN + "base " + Fore.WHITE + "of the " + Fore.BLUE + "Triangle: " + Fore.MAGENTA))
        height_triangle = int(input(Fore.WHITE+"Enter the " + Fore.GREEN + "height " + Fore.WHITE + "of the " + Fore.BLUE + "Triangle: " + Fore.MAGENTA))

        area_triangle = (base_triangle * height_triangle) / 2

        time.sleep(1)
        print(Fore.WHITE+"To calculate the " + Fore.GREEN + "perimeter " + Fore.WHITE + "of the " + Fore.BLUE + "Triangle" + Fore.WHITE + " , just add the value of the sides altogahter!")
        time.sleep(0.5)
        animation()

        print(Fore.RED + "--------------------------------------------------------------------------"+Fore.WHITE + 
              "\nthe" + Fore.GREEN + " area " + Fore.WHITE + "of the Triangle is: " + Fore.GREEN + str(area_triangle))
        
    
    
    elif choice == "8":
        side_square = int(input(Fore.WHITE+"Enter the " + Fore.GREEN + "side " + Fore.WHITE + "of the " + Fore.BLUE + "Square: " + Fore.MAGENTA))

        area_square = side_square ** 2
        perimeter_square = side_square * 4

        animation()

        print(Fore.RED + "--------------------------------------------------------------------------"+Fore.WHITE + 
              "\nthe" + Fore.GREEN + " area " + Fore.WHITE + "of the Square is: " + Fore.GREEN + str(area_square)+
              Fore.WHITE+"\nthe" + Fore.GREEN + " perimeter " + Fore.WHITE + "of the Square is: " + Fore.GREEN + str(perimeter_square))
        
    elif choice == "9":
        height_trapezoid = int(input(Fore.WHITE + "Enter the " + Fore.GREEN + "height" + Fore.WHITE + "of the " + Fore.BLUE + "Trapezoid: "))
        BASE_trapezoid = int(input(Fore.WHITE + "Enter the " + Fore.GREEN + "bigger base " + Fore.WHITE + "of the " + Fore.BLUE + "Trapezoid: "))
        base_trapezoid = int(input(Fore.WHITE + "Enter the " + Fore.GREEN + "smaller base " + Fore.WHITE + "of the " + Fore.BLUE + "Trapezoid: "))
        base_trapezoid_3 = int(input(Fore.WHITE + "Enter the " + Fore.GREEN + "3rd base " + Fore.WHITE + "of the " + Fore.BLUE + "Trapezoid: "))
        side_trapezoid = int(input(Fore.WHITE + "Enter the " + Fore.GREEN + "Side " + Fore.WHITE + "of the " + Fore.BLUE + "Trapezoid: "))

        area_trapezoid = int(BASE_trapezoid + base_trapezoid) * (height_trapezoid / 2)
        perimeter_trapezoid = int(BASE_trapezoid + base_trapezoid) + (side_trapezoid + base_trapezoid_3)

        animation()

        print(Fore.RED + "--------------------------------------------------------------------------"+Fore.WHITE + 
              "\nthe" + Fore.GREEN + " area " + Fore.WHITE + "of the Trapezoid is: " + Fore.GREEN + str(area_trapezoid)+
              Fore.WHITE+"\nthe" + Fore.GREEN + " perimeter " + Fore.WHITE + "of the Trapezoid is: " + Fore.GREEN + str(perimeter_trapezoid))
        
    elif choice == "10":
        factorial1 = int(input("Enter a number: " + Fore.MAGENTA))

        factorated = math.factorial(factorial1)

        animation()

        print("------------------------------------------------------------------\n" + Fore.WHITE + "the factoration of " + Fore.YELLOW + str(factorial1) + Fore.WHITE + " is: " + Fore.GREEN + str(factorated))

    elif choice == "11":
        print("Choose your 3D shape:")

        print(Fore.GREEN + "1. " + Fore.WHITE + "Cube")
        print(Fore.GREEN + "2. " + Fore.WHITE + "Sphere")
        print(Fore.GREEN + "3. " + Fore.WHITE + "Tetrahedrum (3D triangle)")
        print(Fore.GREEN + "4. " + Fore.WHITE + "cylinder")

        choice_3D = input(Fore.YELLOW + "Enter your choice: ")

        if choice_3D == '1':
            cube_length = int(input(Fore.WHITE + "Enter the length: " + Fore.MAGENTA))
            cube_width = int(input(Fore.WHITE + "Enter the width: " + Fore.MAGENTA))
            cube_height = int(input(Fore.WHITE + "Enter the height: " + Fore.MAGENTA))

            cube_area = (cube_length * cube_width) * cube_height
            # cube_P = ((cube_length + cube_width) * 2) + (cube_height * 4)
            cube_P = 4 * (cube_length + cube_width + cube_height)

            animation()

            print(Fore.RED + "--------------------------------------------------------------------------"+Fore.WHITE + 
              "\nthe" + Fore.GREEN + " area " + Fore.WHITE + "of the Cube is: " + Fore.GREEN + str(cube_area)+
              Fore.WHITE+"\nthe" + Fore.GREEN + " perimeter " + Fore.WHITE + "of the Cube is: " + Fore.GREEN + str(cube_P))
            
        elif choice_3D == '2':
            Sphere_radius = int(input(Fore.WHITE + "Enter the radius of the Sphere: " + Fore.MAGENTA))

            sphere_Value_V = ((4 / 3) * pi * (Sphere_radius ** 3))
            sphere_V = round(sphere_Value_V, 2)
            sphere_Value_P = 4 * pi * (Sphere_radius ** 2)
            sphere_P = round(sphere_Value_P, 2)
            

            animation()

            print(Fore.RED + "--------------------------------------------------------------------------"+Fore.WHITE + 
              "\nthe" + Fore.GREEN + " Volume " + Fore.WHITE + "of the Sphere is: " + Fore.GREEN + str(sphere_V)+
              Fore.WHITE+"\nthe" + Fore.GREEN + " surface area " + Fore.WHITE + "of the Sphere is: " + Fore.GREEN + str(sphere_P))


        elif choice_3D == '3':
            edge_Tetra = int(input(Fore.WHITE+"Enter the edge of the tetrahedrum or whatever: " + Fore.MAGENTA))
            tetra_volume = (edge_Tetra ** 3) / (6 * (math.sqrt(2)))
            tetra_surface = (math.sqrt(3)) * (edge_Tetra ** 2)

            animation()

            print(Fore.RED + "--------------------------------------------------------------------------"+Fore.WHITE + 
              "\nthe" + Fore.GREEN + " Volume " + Fore.WHITE + "of the Tetrahedrum is: " + Fore.GREEN + str(tetra_volume)+
              Fore.WHITE+"\nthe" + Fore.GREEN + " surface area " + Fore.WHITE + "of the Tetrahedrium is: " + Fore.GREEN + str(tetra_surface))
        

        elif choice_3D == '4':
            radius_cyl = int(input(Fore.WHITE+"Enter the radius of the cylinder: " + Fore.MAGENTA))
            height_cyl = int(input(Fore.WHITE+"Enter the height of the cylinder: " + Fore.MAGENTA))

            volume_cyl = (pi * (radius_cyl ** 2)) * height_cyl
            surface_cyl = 2 * (pi * radius_cyl * height_cyl) + (2 * pi * (radius_cyl ** 2))

            animation()

            print(Fore.RED + "--------------------------------------------------------------------------"+Fore.WHITE + 
              "\nthe" + Fore.GREEN + " Volume " + Fore.WHITE + "of the Cylinder is: " + Fore.GREEN + str(volume_cyl)+
              Fore.WHITE+"\nthe" + Fore.GREEN + " surface area " + Fore.WHITE + "of the Cylinder is: " + Fore.GREEN + str(surface_cyl))
        


            
        else:
            print(Fore.RED + "Invalid value. choose between 1, 2, 3, etc.")
            
        



    
    #-----------------------------------------------------------------------------------------------------

    else:
        # Invalid choice
        print(Fore.RED + "Invalid choice. Please enter either 1, 2, 3, etc." + Fore.WHITE + "\nDONT USE THIS AGAIN STUPID AHH GUY")  

    print(Fore.CYAN + "\nThank you for using the Area Calculator 2000!" + Fore.RESET)


#------------------------------------------------------------------------------------------------------------------------------------------------------------


while True:
    # Call the calculator function
    calculator()

    # Ask the user if they want to restart or exit
    restart = input(Fore.WHITE + "\nDo you want to restart the calculator? (yes/no): " + Fore.YELLOW).lower()

    if restart != "yes":
        print(Fore.CYAN + "\nThank you for using the Area Calculator 2000!")
        break  # Exit the loop if the user doesn't want to restart

#-------------------------------------------------------------------------------------------

# age = int(input("Enter your age: " + Fore.BLUE))  

# if age >= 18:  
#     print(Fore.WHITE + "mitooni")  
# else:
#     print("boro biroon bache sal")  
#https://t.me/rohamacademypython
