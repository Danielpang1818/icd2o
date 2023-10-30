#1
def middleThree(s):
        middle_index = len(s) // 2
        middle_chars = s[middle_index - 1:middle_index + 2]
        return middle_chars

print(middleThree("aoaoaoa"))

#2
def lastchars(s, a):
        first = s[0:1]
        last = a[len(s)-1:len(s)]
        return first + last
print(lastchars("lol","yes"))

#3
def swap(s):
        result = s[len(s):len(s)-2] + s[len(s):len(s)]
