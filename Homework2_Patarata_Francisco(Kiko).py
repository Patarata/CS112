#Problem 1
#(1)
x = 7
y = 9
print(x > 5)
#(2)
x = 7
y = 9
print((x > 5) and (y < 20))
#(3)
x = 7
y = 9
print((x > 10) and (y < 20))
#(4)
x = 7
y = 9
print((x > 10) or (y < 20))
#(5)
x = 7
y = 9
print((x > 10) or (y > 20))
#(6)
x = 7
y = 9
print(not(x > 10))
#(7)
x = 7
y = 9
print(not((x > 10) and (Y < 20)))
#Problem 2
#1: y = 99
x = 10
if x > 5:
    y = x**2 - 1
elif x >= 5 and x <=10:
    y = 2*x
else:
    y = 2**x
print(y)
#2: y = 5
x = 25
if x < 20:
    y = 0.1 * x
elif x <= 50:
    y = 0.2 * x
else:
    y = 0.3 * x
print(y)
#3: y = 2
x = 5
if x > 10:
    y = x*2
elif x == 10:
    y = x + 5
else:
    y = x - 3
print(y)
#Problem 3
def exam_score_extra_points(exam, extra):
    if exam + extra >= 80:
        print("Passed")
    else:
        print("Failed")
exam_score = float(input("What was your exam score? "))
extra_points = float(input("How many extra points? "))
exam_score_extra_points(exam_score, extra_points)
#Problem 4
uni_size = int(input("How many students are enrolled in the university? "))
if 3000 <= uni_size <= 16000:
    print("The university is medium sized.")
else:
    print("The university is not medium sized.")
#Problem 5
n_hours = int(input("How many hours do you work per week? "))
n_years = int(input("How many years have you worked for the company? "))
if n_hours >= 40 and n_years >= 2:
    print("You are eligible for benefits!")
elif n_hours >=30 and n_years>= 5:
    print("You are eligible for benefits! ")
else:
    print("You are not eligible for benefits... ")
#Problem 6
password = input("Input password: ")
if len(password) < 8:
    print("Weak password ")
elif 8 <= len(password) <= 12:
    print("Moderate password ")
else:
    print("Strong password ")
#Problem 7
age = int(input("Age: "))
if 0 <= age <= 2:
    print("Free")
elif 3 <= age <= 12:
    print("$10")
elif 13 <= age <= 19:
    print("$15")
elif 20 <= age <= 64:
    print("$20")
else:
    print("$8")
#Problem 8
payment = float(input("Money spent: "))
if payment > 200:
    print(payment * 0.8)
elif 120 <= payment <= 200:
    print(payment * 0.85)
elif 80 <= payment < 120:
    print(payment * 0.9)
else:
    print(payment)
#Problem 9
package_weight = float(input("What is the weight of the package? "))
destination = input("Zone 1/ Zone 2? ")
prime = input("Prime member? (Yes/No) ")
if prime == "Yes":
    print("Free Shipping ")
elif destination == "Zone 1" and package_weight <= 10:
    print("Shipping is $10 ")
elif destination == "Zone 1" and package_weight >= 10:
    print("Shipping is $20 ")
elif destination == "Zone 2" and package_weight <= 10:
    print("Shipping is $30 ")
elif destination == "Zone 2" and package_weight >= 10:
    print("Shipping is $50 ")
else:
    print("Please input the correct information")
#Problem 10
fam_income = int(input("What is your family income? "))
if fam_income <= 40000:
    print("Full assistance")
elif 40001 <= fam_income <= 70000:
    print("Partial assistance")
else:
    print("No assistance")
#Problem 11
n = float(input("Give me a number: "))
import math
print(math.sqrt(n))
#problem 12
n_minutes = int(input("How many minutes? "))
n_seconds = n_minutes * 60
print(str(n_seconds) + " Seconds")
#Problem 13
bill = float(input("Amount on bill: "))
tip = int(input("Percentage tip: "))
final = bill * (1 + (tip / 100))
print(final)
#Problem 14
speed = int(input("How fast were you going? "))
spd_limit = int(input("what was the speed limit? "))
if speed <= spd_limit:
    print("No fine ")
elif speed <= (spd_limit + 10):
    print("$50 Fine ")
elif speed > (spd_limit + 10):
    print("$100 Fine ")
else:
    print("Input the correct information...")
#Problem 15
def price_movies(age):
    if age < 5:
        print("free")
    elif 6 < age < 12:
        print("$15")
    elif 12< age < 64:
        print("$20")
    else:
        print("$10")
price_movies(int(input("How old are you ")))
#Problem 16
def bank_withdrawal(balance, withdrawal_amount):
    if balance >= withdrawal_amount:
        print(f'You will be left with ${balance - withdrawal_amount}')
    else:
        print('Insufficient funds')
bank_withdrawal(float(input("How much money is in your balance? ")),
                float(input("How much money are you taking out? ")))


