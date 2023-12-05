#create a list
list = [1,2,3,4,5,6,7,8]

#iterate and print the list
for element in list:          # element is the next element in the list
    print(element)          # works very similarily to range

#get the sum of all of the numbers in the list (2 different ways)
    
total = 0
for el in list:
    total += el

print(total)

print(sum(list))

#print only the positive even numbers in the list
list = [23,4,5,23,51,424,67,9,231,-1,2,-3,4,12,4-23,5-246,-24]
print("Positive Even Numbers: ")
for el in list:
    if el % 2 == 0 and el>0:
        print(el)

#get the largest and smaller number in the list
smallest = list[0]
for el in list:
    if el < smallest:
        smallest = el
print(smallest)

print("get biggest:")
highest = list[0]
for el in list:
    if el > highest:
        highest = el
print(highest)

print(min(list))
print(max(list))

#in a list of Strings, get the string that would be considered largest in terms of "alphabetical order"
name_list = ["dev", "riya", "josh", "arees", "alexander", "abraham", "daniel", "zaafir", "ishaan"]
biggest_name = name_list[0]
for el in name_list:
    if el > biggest_name:
        biggest_name = el
print(biggest_name)

print(max(name_list))
print(min(name_list))

# in a list of String, print the string with the longest length 2 ways
longest = name_list[0]
for el in name_list:
    if len(longest) < len(el):
        longest = el

print(longest)

print(max(name_list,key=len))
print(max(name_list))