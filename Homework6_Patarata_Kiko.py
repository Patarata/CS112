'''
Problem 1. Write a function named three largest(alist) that takes a list of numbers as
input. The function should return a list containing the three largest values from alist,
sorted from lowest to highest. If the list contains fewer than three numbers, return the
original list sorted from lowest to highest. For example
three_largest ([8 , 3 , 1 , 9 , 12])
should return [8, 9, 12].
'''

def three_largest(alist):
    alist.sort()
    return alist[-3:]

print(three_largest ([8 , 3 , 1 , 9 , 12]))

'''
Problem 2. Write a function named find median(alist) that takes a list of numbers alist
as input. The function should return the median value of this list. Recall that the median
is defined as follows
• If the list has an odd number of elements: The median is the middle value in the
sorted list.
• If the list has an even number of elements: The median is the average of the two
middle values.
For example
print ( find_median ([7 , 1 , 4]) )
should return 4 and
print ( find_median ([7 , 1 , 4 , 6]) )
should return 4+6
2 = 5.
'''

def find_median(alist):
    if len(alist) == 0:
        return None
    elif len(alist) == 1:
        return alist [0]
    else:
        alist.sort()
        if len(alist)%2 ==0:
            middle_index1 = len(alist) // 2 - 1
            middle_index2 = len(alist) // 2
            median = (alist[middle_index1] + alist[middle_index2]) // 2
            return alist[median]
        elif len(alist)%2 !=0:
            middle_index = len(alist) // 2
            return alist[middle_index]
print(find_median([7, 1, 4]))


'''
Problem 3. Write a function named sort by price(products) that takes a list of tuples,
where each tuple contains a product name and its price (e.g., (”apple”, 1.50)). The function
should return a new list of these products sorted by their price. For example
sort_by_price ([(" banana ", 1.5) , (" apple ", 2.91) , (" orange ", 2.25)])
should return
[(" banana ", 1.5) , (" orange ", 2.25) , (" apple ", 2.91) ].
To solve this problem, you need to create another function say, get price(a product) that
takes a product as an input and returns its price. See the practice problem file for some
more similar examples.
'''


def sort_by_price(products):
    list_sort = sorted(products, key= get_price)
    return list_sort

def get_price(a_product):
        return a_product[-1]
print(sort_by_price([(" banana ", 1.5) , (" apple ", 2.91) , (" orange ", 2.25)]))

'''
Problem 4. Write a function named sort names(name list) that takes a list of names
name list as input. The function should return a new list with these names sorted in
alphabetical order, ignoring case sensitivity (recall that, in Python lowercase letters are
greater than all uppercase letters.)
For example sort_names ([" anne ", " charlie ", " David ", " Armin "])
should return [”anne”, ”Armin”, ”charlie”, ”David”].
'''


def sort_names(name_list):

    list_sort = sorted(name_list, key=str.lower)
    return list_sort

print(sort_names([" anne ", " charlie ", " David ", " Armin "]))

'''
Problem 5. Write a function named sort title(alist) that takes a list of book titles as
input. The function should return a new list with these titles sorted by the number of
words in each title. For example
alist = ["For whom the bell tolls ", "The old man and the sea", " Please look after mom", " Siddhartha "]
print ( sort_title ( alist ) )
should return
[" Siddhartha ", " Please look after mom", "For whom the bell tolls ",
"The old man and the sea"].
'''

alist = ["For whom the bell tolls ", "The old man and the sea", " Please look after mom", " Siddhartha "]
def sort_title(alist):
    list_sort = sorted(alist, key=len)
    return list_sort
print(sort_title(alist))

'''
Problem 6. Write a function named choose best book(books and ratings) that takes a
list of tuples, where each tuple contains a book title and its rating. The function should
return the name of the book with the highest rating. For simplicity, assume that all the
ratings are different. For example
books_and_ratings = [(" Siddhartha ", 4.9) , ("The Old Man and the Sea", 4.7) , ("For Whom the Bell Tolls ", 4.8) , (" Please Look After Mom", 4.6)]
print ( choose_best_book ( books_and_ratings ) )
should return ”Siddhartha”.
'''

books_and_ratings = [(" Siddhartha ", 4.9) , ("The Old Man and the Sea", 4.7) , ("For Whom the Bell Tolls ", 4.8) , (" Please Look After Mom", 4.6)]
def choose_best_book(books_and_ratings):
    list_sort = sorted(books_and_ratings, key=rating)
    return list_sort [-1][0]

def rating(books_and_ratings):
    return books_and_ratings[-1]

print(choose_best_book(books_and_ratings))

'''
Problem 7.
(1) Write a function named recursive sum(alist) that takes a list of numbers as input
and returns the sum of the squares of all elements in the list. For example
alist = [1 ,2 , -3]
recursive_sum ( alist )
should return 12 + 22 + (−3)2 = 14.
(2) Write another function non recursive sum(alist) to achieve the same goal.
'''
alist = [1 ,2 , -3]
def recursive_sum(alist):
    if len(alist) == 0:
        return 0
    elif len(alist) > 0:
        return recursive_sum(alist[1:]) + alist[0]**2
print(recursive_sum(alist))

def non_recursive_sum(alist):
    count = 0
    for item in alist:
        count = count + item **2
    return count
print(non_recursive_sum(alist))


'''
Problem 8.
(1) Write a function name recursive sum power of two(n) that takes a positive integer
n as an input and returns the sum of the first n-powers of 2
1 + 2 + 22 + . . . + 2n−1

For example
print ( recursive_sum_power_of_two (4) )
should return 15 because 20 + 21 + 22 + 23 = 15.
(2) Write another non-recursive function to achieve the same goal.
Remark 2.1. Can you predict the general formula for the sum
1 + 2 + 22 + . . . + 2n−1
.

'''


def recursive_sum_power_of_two(n):
    if n == 0:
        return 0
    else:
        return 2**(n-1) + recursive_sum_power_of_two(n-1)

print(recursive_sum_power_of_two(4))

def sum_power_two(n):
    count = 0
    for i in range(n):
        count += 2**i
    return count
print(sum_power_two(4))

'''
Problem 9.
(1) Write a recursive function recursive count vowels(s) that takes a string s as input
and returns the number of vowels (a, e, i, o, u) in s, ignoring case.
(2) Write a non-recursive function to achieve the same goal
'''

def recursive_sum_vowels(s):
    if s == '':
        return 0
    elif s[0].lower() in "aeiou":
        return 1 + recursive_sum_vowels(s[1:])
    else:
        return 0 + recursive_sum_vowels(s[1:])
print(recursive_sum_vowels("Banana"))


def sum_vowels(s):
    count = 0
    for c in s:
        if c.lower() == 'a' or c.lower() == 'e' or c.lower() == 'i' or c.lower() == 'o' or c.lower() == 'u':
            count += 1
        else:
            count = count
    return count
print(sum_vowels("Banana"))

'''
Problem 10.
(1) Write a recursive function recurive sum of powers(n, k) that computes the sum of
the first n integers raised to the power of k.
1
k + 2k + . . . + n
k
.
For example
sum_of_powers (3 , 2)
should return 14 because 12 + 22 + 32 = 14.
(2) Write a non-recursive version to achieve the same goal.
3
(3) Use list comprehension and one of your functions to calculate the ratio
1
k + 2k + . . . + n
k
nk+1 ,
for k = 3 and n ∈ [10, 102
, 103
, 104
, 105
, 106
].
Remark 2.2. What do you notice about these ratios when n gets bigger? Welcome to
calculus!
'''

def recursive_sum_of_powers(n, k):
    if n == 0 :
        return 0
    else:
        return n**k + recursive_sum_of_powers(n-1, k)
print(recursive_sum_of_powers(3,2))

def sum_of_powers(n, k):
    count = 0
    for i in range(1, n+1):
        count += i**k
    return count
print(sum_of_powers(3, 2))

#Cant do 3...

'''
Problem 11. An arithmetic progression is a sequence of numbers such that the difference
from any succeeding term to its preceding term remains constant throughout the sequence.
The constant difference is called the common difference of that arithmetic progression
(often denoted by d). For example
1, 4, 7, 10, 13, . . .
is an arithmetic progression with d = 3. An arithmetic sequence can be defined recursively
as follows
a0 = a, an = an−1 + d.
In the above example, a = 1, d = 3.
(1) Write a recursive function arithmetic sequence(a, d, n) that takes the first team
(a), the difference (d), and the index (n) as input and returns the n-th term of the
corresponding arithmetic sequence. For example
arithmetic_sequence (1 , 3 , 4)
should return 13.
(2) Write a non-recursive function to achieve the same goal. Hint: You can create a
sequence [a0, a1, . . . , an−1] using the append method (creating this list is not absolutely necessary but you might find it more intuitive.)
'''

def arithmetic_sequence(a, d, n):
    if n == 0:
        return a
    else:
        return d + arithmetic_sequence(a, d, n-1)
print(arithmetic_sequence(1, 3, 4))

def a_sequence(a, d, n):
    count = a
    for i in range(1, n+1):
        count += d
    return count
print(a_sequence(1, 3, 4))


'''
Problem 12. The Lucas sequence is defined as follows, L0 = 2, L1 = 1 and for n ≥ 2
L(n) = L(n − 1) + L(n − 2).
The first few terms of this sequence are
2, 1, 3, 4, 7, 11, . . .
(1) Write a recursive function named lucas(n) that returns that n-th Lucas number.
(2) Write a non-recursive version to achieve the same goal.
So far, we have learned how recursion works for linear recursion. The same principle
works for non-linear recursive relations as well.
'''

def lucas(n):
    if n==0:
        return 2
    elif n ==1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
print(lucas(5))

def nr_lucas(n):
    a0 = 2
    a1 = 1
    temporary = 0
    if n ==0:
        return a0
    elif n == 1:
        return a1
    for i in range(2, n+1):
        temporary = a0
        a0 = a1
        a1 = a1+ temporary

    return a1
print(nr_lucas(5))

'''
Problem 13. Let an be the sequence defined as follows
a(0) = 1, a(n) = a(n − 1)2 + 1.
The first few terms of this sequence are
1, 2, 5, 26, 677 . . .
(1) Write a recursive function named sequence a(n) that returns that n-th term of this
sequence.
(2) Write a non-recursive version to achieve the same goal.
'''

def sequence_a(n):
    if n == 0:
        return 1
    else:
        return sequence_a(n-1)**2 +1
print(sequence_a(3))

def nr_sequence(n):
    a = 1
    if n ==0:
        return 1
    for i in range(1, n+1):
        a = a**2 +1
    return a
print(nr_sequence(3))


'''
Problem 14. Let an be the sequence defined as follows: b0 = b1 = 1 and
bn =
b
2
n−1 + 2
bn−2
.
The first few terms of this sequence are
1, 1, 3, 11, 41, 153.
(1) Write a recursive function named sequence b(n) that returns that n-th term of this
sequence.
(2) Write a non-recursive version to achieve the same goal.

'''


def sequence_b(n):
    if n == 0 :
        return 1
    elif n ==1:
        return 1
    else:
        return ((sequence_b(n-1))**2 +2) // (sequence_b(n-2))
print(sequence_b(4))

def nr_sequence_b(n):
    b0 = 1
    b1 = 1
    temporary = 0
    if n ==0:
        return 1
    elif n ==1:
        return 1
    for i in range(2, n+1):
        temporary = b0
        b0 = b1
        b1 = (b1**2 + 2) //  temporary
    return b1
print(nr_sequence_b(5))


