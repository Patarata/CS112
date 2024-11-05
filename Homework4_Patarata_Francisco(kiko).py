#Problem 1. Determine the output of the following code:
#(1):The
#(2): cat
#(3):com /r/ pyth
#(4):reddit .com /r/ python
from Homework3 import a_list


#Problem 2. Write a function called odd sum(a list) that takes a list of integers as an
#input. The function will return the sum of all odd numbers in the list. For example
#odd_sum ([ -1 , 2 , -4 , 3 , 5])
#should return 7.

def odd_sum_list(a_list):
    total = 0
    for n in a_list:
        if n%2 != 0:
            total = total + n
    return total
a_list = [ -1 , 2 , -4 , 3 , 5]
print(odd_sum_list(a_list))


#Problem 3. Write a function called count string(a list) that takes a list and returns the
#number of strings in the list. For example
#count_string ([" Hello ", 4 , "5", 5.5])
#should return 2 since there are two strings in this list.

def count_string(a_list):
    count = 0
    for element in a_list:
        if type(element) == str:
            count = count + 1
    return count

print(count_string([" Hello ", 4 , "5", 5.5]))


#Problem 4. Write a function print characters(s) that takes a string and prints each vowel
#character on a new line.

def print_characters(s):
    for c in s:
        if c == 'a' or c== 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c== 'E' or c == 'I' or c == 'O' or c == 'U':
            print(c)
print(print_characters("I love fruits"))


#Problem 5. Write a function called first equal last(string) that takes a string as a string as
#input and returns True if the first and last characters of this string are the same. Otherwise,
#return False. For example,
#first_equal_last (" hello ")
#should return False while
#first_equal_last ("dad ")
#should return True.

def first_equal_last(s):
    return s[0] == s[-1]
print(first_equal_last('Hello'))

#Problem 6. Write a function called print odd length(a list) that takes a list of strings as
#input and prints out all strings with odd lengths in the list. For example
#print_odd_length ([ ’apple ’, ’orange ’, ’banana ’])

def print_odd_length(a_list):
    for item in a_list:
        if len(item) % 2 != 0:
            print(item)
print_odd_length([ 'apple', 'orange', 'banana'])

#Problem 7. Write a function called numeric sum(a list) that takes a list as input and
#returns the sum of all numeric values in the list (a numeric value could be either an integer
#or a floating number). For example
#numeric_sum ([" Hello ", 5 , 6.1 , " Apple "])
#should return 11.1

def numeric_sum(a_list):
    total=0
    for item in a_list:
        if type(item) == float or type(item) == int:
            total = total + item
    return total
print(numeric_sum([" Hello ", 5 , 6.1 , " Apple "]))

#Problem 8. Write a function print reverse(s) that takes a string and prints each character
#in reverse order, starting from the last character and ending with the first. For example
#print_reverse (" test ")
#should print t, s, e,t in that order

def print_reverse(s):
    print(s[::-1])
print_reverse('test')

#Problem 9. Write a function named longest string(a list) that takes a list of strings as
#input and returns the longest string from the list. If there are multiple strings of the same
#length, return the one that appears first. For example
#longest_string ([" Python ", "is", "so", "fun ", "and ", " awesome "])
#should return “awesome”.

def longest_string(a_list):
    long = ''
    for item in a_list:
        if len(item) > len(long):
            long = item
    return long
print(longest_string([" Python ", "is", "so", "fun ", "and ", " awesome "]))

#Problem 10. Write a function substring(s, start, end) that takes a string s and two
#indices start and end, and returns the substring of s from index start to end (inclusive).
#For example
#substrings (" Python is awesome ", 1 , 10)
#should return “ython is a”

def substrings(s, start, end):
    return s[start:end+1]
print(substrings("Python is awesome", 1 , 10))

#Problem 11. Write a function remove first and last(s) that takes a string s and returns
#a new string with the first and last characters removed. For example
#remove_first_and_last (" banana ")
#should return “anan”. Recall that we can use a negative index to slice a string.

def remove_first_and_last(s):
    return s[1:-1]
print(remove_first_and_last('banana'))

#Problem 12. Write a program that asks a user for their name and then prints the first
#letter of their name.

name = input('whats your name: ')
print(name[0])

#Problem 13. Write a function called middle character(s) that returns the middle character(s) of the string s. If the length of s is odd, return the middle character. If the length
#of s is even, return the two middle characters.
#middle_character (" mango ")
#should return ‘n’ and
#middle_character (" orange ")
#should return ‘an’.
def middle_character(s):
    mid = int(len(s) / 2)
    if len(s)%2 ==0:
        return s[mid-1:mid+1]
    elif len(s)%2 !=0:
        return s[mid]
print(middle_character('orange'))
print(middle_character('mango'))

#Problem 14. Write a function find index(a string, char) that returns the index of the last
#occurrence of char in the string a string. For example, find index(“banana”, “a”) should
#return 5.

def find_index(a_string, char):
    for index in range(len(a_string) -1, -1, -1):
        if char == a_string[index]:
            return index
print(find_index('banana', 'a'))


#Problem 15. Write a function called name end with y(a list) that takes a list of names
#as input and returns the number of names that end with the letter y.
#For example called name end with y([‘Jenny’, ‘John’, ‘Amy’]) should return 2.


def name_end_with_y(a_list):
    count = 0
    for item in a_list:
        if item[-1] == 'y':
            count = count + 1
    return count
print(name_end_with_y(['Jenny', 'John', 'Amy']))

#Problem 16. Create a function named count that accepts a string and a letter as arguments, then returns the count of that letter in the string. For example, if the function call
#was count(“banana”, “a”) it would return 3.

def count(s, letter):
    count_letter = 0
    for c in s:
        if c == letter:
            count_letter = count_letter +1
    return count_letter
print(count('banana', 'a'))


#Problem 17. Write a function num digits(n) that will return the number of digits in an
#integer n. Hint: Convert n into a string.

def num_digits(n):
    length = len(str(n))
    print(length)
num_digits(42657)

#Problem 18. Write a Python function sum of digits(n) that takes an integer n and returns
#the sum of its digits. For example, sum of digits(132) should return 6.

def sum_of_digits(n):
    count=0
    for index in str(n):
        count = count + int(index)
    return count
print(sum_of_digits(134556))

#Problem 19.
#(1) Given area code = 60045, format it as “area code: 60045”.
#(2) Given invoice number = 3456, format it with the prefix ”INV-” so it appears as
#”INV-3456”.
#(3) Given name =“John Doe” and title = “Dr.”, format it as “Dr. John Doe”.
area_code = 60045
print(f'area code: {area_code}')

invoice_number = 3456
print(f'INV-{invoice_number}')

name = 'John Doe'
title = 'Dr. '
print(f'{title + name}')

#Problem 20. A palindrome word is a word that reads the same forwards and backward.
#For example, “radar”, “level”, “Dad” are palindrome while “hello” is not. Write a program
#that takes a word and check if it is a palindrome. Note that “Dad” works because we don’t
#distinguish between uppercase and lowercase characters.

word = input('is it a palindrome: ')
if word.lower() == word.lower()[::-1]:
    print('true')
elif word.lower() != word.lower()[::-1]:
    print('false')

