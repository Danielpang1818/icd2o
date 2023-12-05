# number 1
list = ["apple", "kiwi", "banana", "strawberry", "blueberry"]
average = float((len(list[0]) + len(list[1]) + len(list[2]) + len(list[3]) + len(list[4])) /5)
print (average)
 
#number 2
arr = ["level", "python", "radar", "civic", "list"]
count=0
for el in arr:
    isPalindrome = True
    for i in range(len(el)):
        if el[i] != el[len(el) - i - 1]:
            isPalindrome = False
    if isPalindrome:
        count+=1
print(count)
 
#number 3
arr = ["hello", "world", "of", "python", "programming"]
new_string = ''
for i in arr:
    new_string += i + ' '
print (new_string)
 
#number 4
def count_vowels(word):
    vowels = "aeiou"
    return sum(1 for char in word if char in vowels)
 
def dictionary(word_list):
    vowel_count_dictionary = {}
    for word in word_list:
        vowel_count_dictionary[word] = count_vowels(word)
    return vowel_count_dictionary
 
word_list = ["apple", "banana", "kiwi", "strawberry", "blueberry"]
 
result_dictionary = dictionary(word_list)
print(result_dictionary)
 
#number 5
def alternate_upper(word):
    result = ""
    for i in range(len(word)):
        if i % 2 == 0:
            result += word[i].lower()
        else:
            result += word[i].upper()
    return result
 
def alternate_list(word_list):
    return [alternate_upper(word) for word in word_list]
 
word_list = ["python", "programming", "list", "iteration"]
 
result_list = alternate_list(word_list)
print(result_list)
 
#number 6
starting_list = [2,5,-8,10,-3,7,1,-6]
list1 = []
list2 = []
for i in starting_list:
    if i >= 0:
        list1.append(i)
    elif i < 0:
        list2.append(i)
print(list1, list2)
 
#number 7
def is_fibonacci(sequence):
    for i in range(2, len(sequence)):
        if sequence[i - 2] + sequence[i - 1] != sequence[i]:
            return False
    else:
        return True
 
fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21]
 
result = is_fibonacci(fibonacci_sequence)
 
if result:
    print("the list is a fibonacci sequence!")
else:
    print("the list is not a fibonacci sequence.")
 
#number 8
import math
 
list = [1,4,9,16,25]
new_list = []
for i in list:
    new_list.append (int(math.sqrt(i)))
print(new_list)
 
#number 9
def running_average(numbers):
    total_sum = 0
    averages = []
    count = 0
 
    for num in numbers:
        count += 1
        total_sum += num
        current_average = total_sum / count
        averages.append(current_average)
 
    return averages
 
number_list = [5, 10, 15, 20, 25]
 
result = running_average(number_list)
print(result)
 
#number 10
def consecutive_pairs(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] - numbers[i + 1] == 1:
            return True
    return False
 
number_list = [3, 5, 7, 9, 10, 11, 15]
 
result = consecutive_pairs(number_list)
 
if result:
    print("this list contains consecutive pairs with a difference of 1.")
else:
    print("this list does not contain consecutive pairs with a difference of 1.")