month = int(input())
day = int(input())

if month > 2:
    print("Before")
elif month > 2:
    print("After")
else:
    if day > 18:
        print("After")
    elif day < 18:
        print("Before")
    else:
        print("Special")