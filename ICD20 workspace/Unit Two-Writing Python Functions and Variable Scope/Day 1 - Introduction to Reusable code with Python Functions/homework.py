# Function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        return length * width
    else:
        return "Invalid input. Please provide numeric values for length and width."

# Function to check if a string contains a specific substring
def contains_substring(string, substring):
    if isinstance(string, str) and isinstance(substring, str):
        return substring in string
    else:
        return "Invalid input. Please provide two strings."

# Function to calculate the average of three floats
def average_of_three_floats(num1, num2, num3):
    if all(isinstance(x, float) for x in [num1, num2, num3]):
        return (num1 + num2 + num3) / 3.0
    else:
        return "Invalid input. Please provide three floating-point numbers."

# Function to concatenate two strings
def concatenate_strings(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        return str1 + str2

# Function to calculate the volume of a cube
def volume_of_cube(side_length):
    if isinstance(side_length, (int, float)):
        return side_length ** 3

# Function to check if a number is positive, negative, or zero
def check_number_status(number):
    if isinstance(number, (int, float)):
        if number > 0:
            return "Positive"
        elif number < 0:
            return "Negative"
        else:
            return "Zero"

# Function to calculate the circumference of a circle
def circumference_of_circle(radius):
    if isinstance(radius, (int, float)):
        return 2 * 3.141592653589793 * radius

# Function to count the number of occurrences of a character in a string
def count_char_occurrences(string, char):
    if isinstance(string, str) and isinstance(char, str) and len(char) == 1:
        return string.count(char)

# Function to calculate the percentage of a number
def calculate_percentage(number, percentage):
    if isinstance(number, (int, float)) and isinstance(percentage, (int, float)):
        return (percentage / 100) * number

# Function to find the absolute difference between two numbers
def absolute_difference(num1, num2):
    if all(isinstance(x, (int, float)) for x in [num1, num2]):
        return abs(num1 - num2)

# Function to capitalize the first letter of a string
def capitalize_first_letter(string):
    if isinstance(string, str):
        return string.capitalize()

# Function to calculate the square of a number
def square(number):
    if isinstance(number, (int, float)):
        return number ** 2

# Function to find the maximum of two numbers
def max_of_two(num1, num2):
    if all(isinstance(x, (int, float)) for x in [num1, num2]):
        if num1 > num2:
            return num1
        else:
            return num2

# Function to calculate the square root of a number
def square_root(number):
    if isinstance(number, (int, float)) and number >= 0:
        return number ** 0.5

# Function to find the length of a string
def length(input_data):
    if isinstance(input_data, str):
        return len(input_data)
    
#########################################

#hw1

length = int(input("Input the lenght: "))
width = int(input("Input the width: "))
area = area_of_rectangle(length,width)
print(f"The area of the rectangle is : {round(area,2)}")

#hw2
string = input("input your string: ")
substring = input("Enter a substring: ")
result = contains_substring(string,substring)
print(f"Substring {substring} is present in the string: {result}")

#hw3
num1 = float(input("Input your number: "))
num2 = float(input("Input your number: "))
num3 = float(input("Input your number: "))
average = average_of_three_floats(num1,num2,num3)
print(f"The average is {average:.2f}")

#hw4
string1 = input("Enter string: ")
string2 = input("Enter string: ")
concatenate = concatenate_strings(string1,string2)
print(f"The concatenated string is {concatenate}")

#hw5
side = float(input("What is the side of the cube: "))
volume = volume_of_cube(side)
print(f"The volume of the cube is {volume:.2f} cubic units")

#hw6
number = float(input("Enter a number: "))
status = check_number_status(number)
print(f"The number is: {status}")

#hw7
radius = float(input("What is the radius: "))
circumference = circumference_of_circle(radius)
print(f"The circumference of the circle is {circumference:.2f} units")

#hw8
string = input("Enter a string: ")
character = input("Enter a character: ")
occurence = count_char_occurrences(string,character)
print(f"The character {character} occurs {occurence} times in the string")

#hw9
number = int(input("Enter a number: "))
percent = int(input("Enter a percentage: "))
percentage = calculate_percentage(number,percent)
print(f"{percent} percent of the number is {percentage:.2f}")

#hw10
num1 = float(input("What is the number: "))
num2 = float(input("What is the number: "))
difference = absolute_difference(num1,num2)
print(f"The absolute difference is {difference:.2f}")