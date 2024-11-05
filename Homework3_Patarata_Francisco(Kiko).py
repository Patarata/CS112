#Problem 1. Write a function called poly perimeter that takes in two parameters, len side,
#and num sides, and returns the perimeter of the polygon. The perimeter of a polygon is
#the length of each side times the number of sides. For example, poly perimeter(4,5) should
#return 20.

def poly_meter(len_side, num_side):
    return len_side * num_side

y = poly_meter(int(input('lenght side: ')), int(input('number sides: ')))
print(y)

#Problem 2. Create a function called get hypotenuse that takes in two parameters, a and
#b, which represent the lengths of the two legs of a right triangle. The function should
#return the length of the hypotenuse. Use the Pythagorean theorem
import math
def get_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

y = get_hypotenuse(int(input('side a: ')), int(input('side b:')))
print(f'hypotenuse is ' + str(y))

#Problem 3. Write a function called find distance that takes in four parameters, x1, y1, x2, y2,
#and returns the distance between these two points (x1, y1) and (x2, y2). The distance is
#given by the following formula which is a consequence of the Pythagorean theorem
import math
def find_distance(x1, x2, y1, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

y = find_distance(int(input('Give me x1: ')), int(input('Give me x2: ')), int(input('Give me y1: ')), int(input('Give me y2: ')))
print(y)

#Problem 4. Write a function called total string length that takes in two parameters, str1
#and str2, and returns the total length of these two strings.

def total_string_length(str1, str2):
    return len(str1) + len(str2)

y = total_string_length(input('Input a string: '), input('Input a seconf string: '))
print(f'Total string length is: {y}')

#Problem 5. Write a function called address that combines 3 different string address parameters (city, state, and zip) and returns a user’s address. After the city and state inputs,
#add a comma and a space. For example,
#address (’Seattle ’, ’WA ’, ’98105 ’)
#should return ”Seattle, WA, 98105”.
def address(city, state, zip):
    return '"' + city + ', ' + state + ', ' + zip + '"'
y=address(input('city: '), input('state: '), input('zip: '))
print(y)

#Problem 6. Write a function apply discount(price, is member) that applies a discount
#based on membership status:
#• 10% discount for members.
#• No discount for non-members.
#For example
#apply_discount (100 , True )
#should return 90.

def apply_discount(price, is_member):
    if is_member == 'yes':
        return price * 0.9
    else:
        return price
y = apply_discount(float(input('price: ')), input('Member? (yes/no): '))
print(f'final price is {y}')

#Problem 7. Write a function called shipping price that takes two arguments: weight and
#express and returns shipping cost based on the weight of the package and whether express
#shipping is selected:
#1
#• Standard Shipping:
#– $5 for weights up to 2 lbs
#– $10 for weights above 2 lbs
#• Express Shipping:
#– $10 for weights up to 2 lbs
#– $20 for weights above 2 lbs
#For example
#calculate_shipping_cost (4 , True )
#should return 20.

def shipping_price(weight, express):
    if express == "no" and weight <= 2:
        return 5
    elif express == "no" and weight >= 2:
        return 10
    elif express == "yes" and weight <= 2:
        return 10
    elif express == "yes" and weight >= 2:
        return 20


#Problem 8. Write a function called final price that takes three arguments: price, weight,
#and express and returns the final total price. The final price is the sum of the price and
#the shipping cost which is calculated as follows
#• For purchase prices $100 or more, shipping is free.
#• For purchase prices below $100, the shipping fee is calculated based on the formula
#from the previous problem.
#Your function should call the shipping price from the previous problem.


def final_price(price, weight, express):
    if price > 100:
        return price
    else:
        return price + shipping_price(weight, express)
x = final_price(float(input("price ")), float(input("weight ")), input("express shipping? "))
print(x)



#Problem 9. Write a function countdown to zero(start) that counts down from the given
#start number to 0, printing each number. If the starting number is less than or equal to 0,
#the function should print a message “Enter a positive number”.

def countdown_to_zero(start):
    my_range = range(0, start +1)
    for start in reversed(my_range):
        if start < 0:
            print('input positive number ')
        else:
            print(start)

y = countdown_to_zero(int(input('number to countdown: ')))
print(y)


#Problem 10. Write a function buzz(n) that prints the numbers from 1 to n. For multiples
#of 3, print “Buzz” instead of the number.

def buzz(n):
    my_range = range(1, n+1)
    for item in my_range:
        if item%3 == 0:
            print('Buzz')
        else:
            print(item)

buzz(10)


#Problem 11. Write a function called negative sum(a list) that takes a list as an input.
#The function will return the sum of all negative numbers in the list. For example
#negative_sum ([ -1 , 2 , -3])
#should return −4.

def negative_sum(a_list):
    total = 0
    for item in a_list:
        if item < 0:
            total = total + item
    return total
a_list = [1, 2, 3, 4, 5, 0, -4, -6]
print(negative_sum(a_list))


#Problem 12. Write a function called even positive sum(a list) that takes a list of integers
#as an input. The function will return the sum of all positive even numbers in the list (a
#positive even number is a number that is both positive and even). For example
#negative_sum ([ -1 , 2 , -4 , 3 , 6])


def even_positive_sum(a_list):
    total = 0
    for item in a_list:
        if item > 0 and item%2 == 0:
            total = total + item
    return total
a_list = [1, 2, 3, 4, 5, 0, -4, -6]
print(even_positive_sum(a_list))

#Problem 13. Write a function called maximal element(a list) that takes a list as an input.
#The function will return the maximal element in the list. For example
#negative_sum ([1 , 5 , 2 , 4])

def maximal_element(a_list):
    current = None
    for item in a_list:
        if current is None or item > current:
            current = item
    return current


a_list = [1, 2, 3, 4, 5, 0, -4, -6]
print(maximal_element(a_list))

#Problem 14. Write a function called is prime(n) that checks whether a number is a prime
#number or not. A prime number is a number whose divisors are 1 and itself. For example:
#2, 5, 7, and 11 are prime numbers while 6 is not.

def prime(n):
    my_list = range(1, n+1)
    for item in my_list:
        if item%item == 0 and item%1 == 0:
             print(item)
prime(10)


#Problem 15. Write a function called sum divisors(n) that calculates the sum of all of the
#divisors of n.


def sum_divisors(n):
    my_list = range(1, n+1)
    total = 0
    for item in my_list:
        if n%item == 0:
            total = total + item
    return total

print(sum_divisors(10))



#Problem 16. Write a function called sum square(n) that calculates the sum of the squares
#of all numbers between 1 and n. For example, sum square(1) should return 1 and sum square(2)
#should return 5.

def sum_square(n):
    my_list = range(1, n+1)
    total = 0
    for item in my_list:
         total = total + item**2
    return total

print(sum_square(2))


#Problem 17. An integer n is called a perfect square if n = m2
#for some integer n. For
#example, 4 is a perfect square because 4 = 22
#. On other other hand, 6 is not a perfect
#square. Write a function called is square(n) to check whether a number n is a perfect
#square

def is_square(n):
    my_list = range(1, n+1)
    for item in my_list:
        if n == item**2:
            print('it is perfect square! ')

is_square(9)

#Problem 18. Write a function that prints out all perfect square numbers between 1 and
#100.

def print_perfect_squares():
    for num in range(1, 101):
        if int(num**0.5)**2 == num:
            print(num)

print_perfect_squares()

#Problem 19. Write a function that takes a string as an input and returns True if this
#string contains the lowercase letter h. Otherwise, return False

def fun_string_lower(s):
   for c in s:
       if c == 'h':
           return 'true'
   return 'false'

print(fun_string_lower('aw;ourgbihuwrg'))
