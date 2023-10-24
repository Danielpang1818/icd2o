#functions
import math
def multiply(num1,num2):
    print(f"The product is {num1*num2}")

def volume(radius,height):
    print(f"The volume is {radius**2*math.pi*height:.2f}")

def triangle(tri):
    print(tri)
    print(tri,tri)
    print(tri,tri,tri)
    print(tri,tri,tri,tri)

def sayhello(name):
    print(f"Hey there {name}")

def circlearea(radius):
    print(f"The circle with the radius: {radius} has an area of {radius**2*math.pi:.2f}")

def print_square(character, size):
    print(character)

def calculate_power(number,power):
    print(f"{number} to the power of {power} is {number**power:.2f}")

def triangle_area(base,height):
    print(f"The area of a triangle with a  height and baseof {base} and {height} is {base*height}")

#hw1

num1 = int(input("Enter num: "))
num2 = int(input("Enter num: "))

multiply(num1,num2)

#hw2

radius = int(input("Enter radius: "))
height = int(input("Enter height: "))
volume(radius,height)

#hw3
tri = input("Enter a character: ")
triangle(tri)

#hw4
name = input("Enter name: ")
sayhello(name)

#hw5
radius = float(input("Enter the radius: "))
circlearea(radius)

#hw6
character = input("Enter a character: ")
size = int(input("Enter an input: "))
print_square(character,size)

#hw7
number = int(input("Enter a number: "))
power = int(input("Enter the power: "))
calculate_power(number,power)

#hw8
height = int(input("Enter the height: "))
base = int(input("Enter the base: "))
triangle_area(base,height)