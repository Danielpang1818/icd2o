def print_greeting(name):
    print(f"Hello {name}")

def calculate_area(length, width):
    print(f"The area of the rectangle is {length*width}")

def print_pattern(char):
    print(char)
    print(char)
    print(char)
    print(char)
    print(char)
    print(char)

length = int(input("Enter the Length"))
width = int(input("Enter the width"))
calculate_area(length,width)

person_name = input("Please enter a name: ")
print_greeting(person_name)

char = input("Input your name")
print_pattern(char)
