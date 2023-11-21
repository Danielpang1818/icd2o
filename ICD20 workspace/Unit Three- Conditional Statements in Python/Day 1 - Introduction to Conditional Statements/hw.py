def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed = speed - 5

    if speed <= 60:
        return "No Ticket."

    if 61 <= speed <= 80:
        return "Small Ticket."
    return "Big Ticket."

print(caught_speeding(73, True))

#2 hw
def not_string(s):
    if s[0:4] == "not ":
        return s
    return "not " + s
s = input("Enter string: ")
print(not_string(s))

#3hw
def squirrel_play(temp, is_summer):
    if is_summer:
        temp = temp -10
    if 50 <= temp <= 90:
        return True
    return False

print(squirrel_play(99, True))

#4hw
def in1020(a, b):
    if 10 <= a <= 20:
        return True
    elif 10 <= b <= 20:
        return True
    else:
        return False
    
print(in1020(3,13))

#5 hw
def theEnd(s, front):
    if len(s) == 0:
        return "Empty"  
    elif front:
        return s[0]  
    else:
        return s[-1]  
    
print(theEnd("lololo", False))

