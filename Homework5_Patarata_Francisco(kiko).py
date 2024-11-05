#Problem 1. Write a function filter positive even(numbers) that takes a list of integers
#and returns a new list containing only the positive even numbers.
#filter_even ([1 , -2 , -3 , 4 , 5 , 6])
#should return [4, 6]. Note that -2 does not work because it is negative

def filter_positive_even(numbers):
    new_list = []
    for item in numbers:
        if item %2 == 0  and item >0:
            new_list.append(item)
    return new_list
print(filter_positive_even([1 , -2 , -3 , 4 , 5 , 6]))


#Problem 2. Write a function named is empty(a list) that returns True if the list is empty
#and False otherwise.

def is_empty(a_list):
    return a_list == []

print(is_empty([1]))

#Problem 3. Write a function named multiply factor(a list, factor) that returns a list where
#each element in the original list is multiplied by the given factor. For example
#multiply_factor ([1 , 2 , -3] , 2)
#should return [2, 4, -6].

def multiply_factor(alist, factor):
    new_list = []
    for item in alist:
        new_list.append(item * factor)
    return new_list
print(multiply_factor ([1 , 2 , -3] , 2))


#Problem 4. Write a function named numeric values(a list) that takes a list as input and
#returns a new list with only the numeric elements. Numeric values include both integers
#and floating-point numbers. For example:
#numeric_values (["1", " apple ", 1 , 1.2 , -4])
#should return [1, 1.2, −4].

def numeric_values(alist):
    new_list =[]
    for item in alist:
        if type(item) == int or type(item) == float:
            new_list.append(item)
    return new_list
print(numeric_values (["1", " apple ", 1 , 1.2 , -4]))

#Problem 5. Write a function named remove element(a list, element) that takes a list and
#an element as input and returns a new list with all occurrences of that element removed.
#For example
#removed_element ([0 , " test ", 1 , " apple ", 0 , 1.1] , 0)
#should return [“test”, 1, ”apple”, 1.1].

def remove_elements(alist,  element):
    new_list = []
    for item in alist:
        if item != element:
            new_list.append(item)
    return new_list
print(remove_elements([0 , " test ", 1 , " apple ", 0 , 1.1] , 0))

#Problem 6. Write a function uppercase strings(a list) that takes a list of strings and
#returns a new list with all the strings in uppercase. For example
#uppercase_strings ([" Anne ", " Ben", " David "])
#should return [“ANNE”, “BEN”, “DAVID”].

def uppercase_strings(alist):
    new_list = []
    for item in alist:
        new_list.append(item.upper())
    return new_list
print(uppercase_strings ([" Anne ", " Ben", " David "]))

#Problem 7. Write a function last names(full names) that takes a list of full names and
#returns a new list containing all last names. Here, we assume that each full name consists
#of a first name followed by a last name, separated by a space. For example,
#last_names ([" Anne Nguyen ", " David Hilbert ", " Michael Jordan ", "
#Alan Turing "])
#should return [“Nguyen”, “Hilbert”, “Jordan”, ”Turing”]. All of these individuals are
#famous, except for the first one (at least for now!).

def last_names(full_names):
    new_list = []
    for item in full_names:
        new_list.append(item.split()[-1])
    return new_list
print(last_names ([" Anne Nguyen ", " David Hilbert ", " Michael Jordan ", "Alan Turing"]))

#Problem 8. Write a function join strings(a list) that takes a list of strings and joins them
#into a single string, separated by spaces.
#join_strings (["I", " Love ", " Lake ", " Forest ", " College "])
#should return “I Love Lake Forest College”.

def join_strings(alist):
    sentence = ''
    for item in alist:
        sentence = sentence + item
    return sentence

print(join_strings(["I", " Love ", " Lake ", " Forest ", " College "]))

#Problem 9. Write a function longest string(a list) that takes a list of strings and returns
#the longest string. For example
#longest_string ([" apple ", " banana ", " mango "])
#should return “banana”.

def longest_string(alist):
    longest = ''
    for item in alist:
        if len(item) > len(longest):
            longest = item
    return longest
print(longest_string([" apple ", " banana ", " mango "]))

#Problem 10. Given a list of circle radii, create a new list containing the corresponding
#areas of the circles, rounded to one decimal place. For example, if the list is
#radii = [1 ,2 ,3]
#then, the corresponding areas should be [3.1, 12.6, 28.3].

import math
radii = [1 ,2 ,3]
area = []
for item in radii:
    area.append(round((item**2)*math.pi, 1))
print(area)

#Problem 11. From a list of integers, create a new list that includes only the odd numbers
#using list comprehension. For example, if the given list is [1, 2, 3, 4, 5, 6], then the new
#list should be [1, 3, 5].

alist = [1, 2, 3, 4, 5, 6]
oddlist =[]
for item in alist:
    if item %2!=0:
        oddlist.append(item)
print(oddlist)

#Problem 12. From a list of strings, create a new list that contains the first letter of each
#string. For example, if the given list is [“Apple”, “Banana”, “Mango”], the new list should
#be [“A”, “B”, “M”].

names = ['Apple', 'Banana', 'Mango']
newlist = []
for item in names:
    newlist.append(item[0])
print(newlist)

#Problem 13. Given a list of words, create a new list containing only those words that are
#shorter than 4 characters. For example, if the list is [“Ant”, “Dog”, “Lion”, ”Fish”]), the
#new list should be [“Ant”, “Dog”].

names = ['Ant', 'Dog', 'Lion', 'Fish']
newlist = []
for item in names:
    if len(item)< 4:
        newlist.append(item)
print(newlist)