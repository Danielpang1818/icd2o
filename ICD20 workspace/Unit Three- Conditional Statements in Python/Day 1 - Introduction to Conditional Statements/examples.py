# Check if a number is positive.
number = int(input("Please enter a number: "))
if number > 0:
    print(f"{number} is positive")

if number <= 0:
    print(f"{number} is not positive")

# Determine if a person can vote (age 18 or older.)
age = int(input("Enter your age: "))

# if age >= 18:
#     not_eligable = ""
# if age < 18:
#     eligable = "eligable"

# print(f"You are eligable to {eligable}vote")

if age >= 18:
    print(f"You can vote")

if age < 18:
    print("You cannot vote")

#Check if a string is empty.
str = input("Please enter a String: ")
if len(str) == 0:
    print("The string is Empty")

if len(str) != 0:
    print("The String is not Empty")

# Write a function that returns the maximum of two numbers
def max_number(a, b):
    if a > b:
        return a
    return b
print(max_number(4,5))
print(max_number(14,5))

# Check if a user's input is equal to a secret password.
def password_checker(password, user_input):
    return user_input == password

pwd = input("Password: ")
secret = "oansfonasofna" 
print(password_checker(secret,pwd))

#Write a function that checks if a number is withen the specific range (1-10 inclusive)
def range_check(num, lower, upper):
    if lower <= num <= upper:
        return "Good you listen to instructions!!!"
    return "ARGHHHH!!!! I am not happy because you DON'T LISTEN"

num = int(input("Please enter a number betweeen 1 and 10: "))
print(range_check(num, 1, 10))

# Write a function that accepts a numberical grade and returns the Letter Grade
def grade_converter(grade):
    if grade >= 80:
        return "A"
     if grade >= 70:
        return "B"
     if grade >= 60:
        return "C"
     if grade >= 50:
        return "D"
    return "F"
 