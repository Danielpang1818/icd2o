# # Python program to demonstrate
# # Creation of List

# # Creating a List
# List = []
# print("Blank List: ")
# print(List)

# # Creating a List of numbers
# List = [10, 20, 14]
# print("\nList of numbers: ")
# print(List)

# # Creating a List of strings and accessing
# # using index
# List = ["Geeks", "For", "Geeks"]
# print("\nList Items: ")
# print(List[0]) #Starts at the first one. It will print Geeks
# print(List[2]) # Goes to the 3rd one. It will print Geeks.

list = []
list.append("hello")
list.append("Steve")
list.append("Abragham")
list.append("chicken")

print(list)
list.append(7)
print(list)

list.insert(2, "Dev")
print(list)
list.remove("chicken")
print(list)

list.pop(1)
print(list)