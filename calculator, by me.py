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


def calculator():
    print(Fore.WHITE + "Welcome to the Area Calculator 2000!")
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

    print(Fore.CYAN + "------------------------------------")

    # Get user choice
    choice = input(Fore.WHITE + "Enter your choice (1, 2, 3, etc.): " + Fore.YELLOW)

    # Handle user's choice
    if choice == "1":
        # Circle Area Calculation
        print(Fore.WHITE + "\nYou chose to calculate the area of a Circle.")
        diameter = int(input(Fore.WHITE + "Enter the diameter of the circle: " + Fore.MAGENTA))
        radius = diameter / 2
        pi = 3.14

        print(Fore.WHITE + "\nCalculating the" + Fore.GREEN + " area " + Fore.WHITE + "of a" + Fore.BLUE + " Circle" + Fore.WHITE + ", Please be patient...")
        time.sleep(3)

        area_circle = (radius ** 2) * pi
        perimeter_circle = diameter * pi

        print("-------------------------------------------------------------------" + Fore.WHITE + "\nThe " + Fore.GREEN + "area" + Fore.WHITE + " of the circle is: " + Fore.BLUE + str(area_circle))
        print("-------------------------------------------------------------------" + Fore.WHITE + "\nThe " + Fore.GREEN + "perimeter" + Fore.WHITE + " of the circle is: " + Fore.BLUE + str(perimeter_circle) + Fore.WHITE)

    elif choice == "2":
        # Rectangle Area Calculation
        print(Fore.WHITE + "\nYou chose to calculate the area of a Rectangle.")
        length = int(input(Fore.WHITE + "Enter the length of the rectangle: " + Fore.MAGENTA))
        width = int(input(Fore.WHITE + "Enter the width of the rectangle: " + Fore.MAGENTA))

        print(Fore.WHITE + "\nCalculating the" + Fore.GREEN + " area " + Fore.WHITE + "of a" + Fore.BLUE + " Rectangle" + Fore.WHITE + ", Please be patient...")
        time.sleep(3)

        area_rectangle = length * width
        perimeter_rectangle = 2 * (length + width)

        print("-------------------------------------------------------------------" + Fore.WHITE + "\nThe " + Fore.GREEN + "area" + Fore.WHITE + " of the rectangle is: " + Fore.BLUE + str(area_rectangle))
        print("-------------------------------------------------------------------" + Fore.WHITE + "\nThe " + Fore.GREEN + "perimeter" + Fore.WHITE + " of the rectangle is: " + Fore.BLUE + str(perimeter_rectangle) + Fore.WHITE)

    elif choice == "3":
        # Rhombus Calculation
        Pdiagonal = int(input(Fore.WHITE + "Please enter the" + Fore.YELLOW + " Smaller Diagonal: " + Fore.MAGENTA))
        Qdiagonal = int(input(Fore.WHITE + "Please enter the" + Fore.YELLOW + " Bigger Diagonal: " + Fore.MAGENTA))
        side_rhombus = int(input(Fore.WHITE + "Please enter the" + Fore.YELLOW + " Side " + Fore.WHITE + "of the Rhombus: " + Fore.MAGENTA))

        print(Fore.WHITE + "\nCalculating the" + Fore.GREEN + " area " + Fore.WHITE + "of a" + Fore.BLUE + " Rhombus" + Fore.WHITE + ", Please be patient...")
        time.sleep(3)

        area_rhombus = int((Pdiagonal * Qdiagonal)) / 2
        perimeter_rhombus = int(side_rhombus * 4)

        print(Fore.WHITE + "the" + Fore.GREEN + " area " + Fore.WHITE + "of the Rhombus is: " + Fore.RED + str(area_rhombus))
        print(Fore.WHITE + "the" + Fore.GREEN + " perimeter " + Fore.WHITE + "of the Rhombus is: " + Fore.RED + str(perimeter_rhombus))

    elif choice == "4":
        # Combination Calculation
        n = int(input(Fore.WHITE + "Enter the number of " + Fore.YELLOW + "Items: " + Fore.MAGENTA))
        r = int(input(Fore.WHITE + "Enter the number of " + Fore.YELLOW + "Slots: " + Fore.MAGENTA))

        print(Fore.WHITE + "\nCalculating the" + Fore.GREEN + " Combinations")
        time.sleep(3)

        combination_ = combination(n, r)

        if r > n:
            print(Fore.RED + "Slots cannot be more than Items")
        else:
            print(Fore.WHITE + "There is " + Fore.GREEN + str(combination_) + Fore.WHITE + " different " + Fore.RED + "combinations " + Fore.WHITE + "of " + Fore.MAGENTA + str(n) + " Items And " + str(r) + " Slots!")

    elif choice == "5":
        # Permutation Calculation
        N = int(input(Fore.WHITE + "Enter the number of " + Fore.YELLOW + "Items: " + Fore.MAGENTA))
        R = int(input(Fore.WHITE + "Enter the number of " + Fore.YELLOW + "Slots: " + Fore.MAGENTA))

        print(Fore.WHITE + "\nCalculating the" + Fore.GREEN + " Permutations")
        time.sleep(3)

        permutation_ = permutation(N, R)

        if R > N:
            print(Fore.RED + "Slots cannot be more than Items")
        else:
            print(Fore.WHITE + "There is " + Fore.GREEN + str(permutation_) + Fore.WHITE + " different " + Fore.RED + "Permutations " + Fore.WHITE + "of " + Fore.MAGENTA + str(N) + " Items And " + str(R) + " Slots!")

    elif choice == "6":
        nn = int(input(Fore.WHITE + "Enter the number of " + Fore.YELLOW + "Items: " + Fore.MAGENTA))
        rr = int(input(Fore.WHITE + "Enter the number of " + Fore.YELLOW + "Slots: " + Fore.MAGENTA))

        print(Fore.WHITE + "\nCalculating the" + Fore.GREEN + " Permutations")
        time.sleep(3)

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
        print(Fore.WHITE + "\nCalculating the" + Fore.GREEN + " area " + Fore.WHITE + "of a" + Fore.BLUE + " Triangle" + Fore.WHITE + ", Please be patient...")
        time.sleep(5)

        print(Fore.RED + "--------------------------------------------------------------------------"+Fore.WHITE + 
              "\nthe" + Fore.GREEN + " area " + Fore.WHITE + "of the Triangle is: " + Fore.GREEN + str(area_triangle))
        
    
    
    elif choice == "8":
        side_square = int(input(Fore.WHITE+"Enter the " + Fore.GREEN + "side " + Fore.WHITE + "of the " + Fore.BLUE + "Square: " + Fore.MAGENTA))

        area_square = side_square ** 2
        perimeter_square = side_square * 4

        print(Fore.WHITE + "\nCalculating the" + Fore.GREEN + " area " + Fore.WHITE + "of a" + Fore.BLUE + " Square" + Fore.WHITE + ", Please be patient...")
        time.sleep(5)

        print(Fore.RED + "--------------------------------------------------------------------------"+Fore.WHITE + 
              "\nthe" + Fore.GREEN + " area " + Fore.WHITE + "of the Square is: " + Fore.GREEN + str(area_square)+
              Fore.WHITE+"\nthe" + Fore.GREEN + " perimeter " + Fore.WHITE + "of the Square is: " + Fore.GREEN + str(perimeter_square))


    
    #-----------------------------------------------------------------------------------------------------

    else:
        # Invalid choice
        print(Fore.RED + "Invalid choice. Please enter either 1, 2, 3, 4, 5, 6, 7 or 8." + Fore.WHITE + "\nDONT USE THIS AGAIN STUPID AHH GUY")  

    print(Fore.CYAN + "\nThank you for using the Area Calculator 2000!" + Fore.RESET)


#------------------------------------------------------------------------------------------------------------------------------------------------------------


while True:
    # Call the calculator function
    calculator()

    # Ask the user if they want to restart or exit
    restart = input(Fore.WHITE + "\nDo you want to restart the calculator? (yes/no): " + Fore.YELLOW).lower()

    if restart != 'yes':
        print(Fore.CYAN + "\nThank you for using the Area Calculator 2000!")
        break  # Exit the loop if the user doesn't want to restart

#-------------------------------------------------------------------------------------------

# age = int(input("Enter your age: " + Fore.BLUE))  

# if age >= 18:  
#     print(Fore.WHITE + "mitooni")  
# else:
#     print("boro biroon bache sal")  
#https://t.me/rohamacademypython
