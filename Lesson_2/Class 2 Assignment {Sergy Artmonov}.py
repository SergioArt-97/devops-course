#A
import random


def bigger_or_smaller(n1,n2):
    if n1 > n2:
        print("BIG")
    else:
        print("small")
x = 10
y = 15
bigger_or_smaller(x,y)
print()

#B
for i in range(5):
    print(i)
print()

#C
random_season = random.randint(1,4)
def pick_a_season(season):
    if season == 1:
        print("summer")
    elif season == 2:
        print("winter")
    elif season == 3:
        print("fall")
    elif season == 4:
        print("spring")
pick_a_season(random_season)
print()

#D
""" 
it will print:
1
2
3
4
5
6
7
8
9
10
10 will be printed last
"""

#E
my_variables = {
    "Age": "27",
    "First letter": "S",
    "D to S convertion": (1, 3.58),
    "Was abroad?": True,
    "Apartment number": 28
}
print("My age is:", my_variables["Age"])
print("the first letter of my name is:", my_variables["First letter"])
print(f"The current conversion of a dollar to shekel is {my_variables["D to S convertion"][0]} dollar to {my_variables["D to S convertion"][1]} Shekels")
print("Was i abroad?", my_variables["Was abroad?"])
print("My apartment number is ", my_variables["Apartment number"])
print()

#F
user_phone_number = input("Please provide me with your phone number: ")
print("phone number", user_phone_number)

#G
def print_hello():
    print("hello")
print_hello()

def calculate():
    print(5 + 3.2)
calculate()
print()

#H
def print_name():
    name = input("Please provide me with your name: ")
    print(name)
print_name()
print()

#I
def calculate2(n1, n2):
    return n1 + n2
print(calculate2(10,12))

def connect_string(s1, s2):
    s3 = s1 + " " +  s2
    return s3

str1 = "Hello"
str2 = "World"
print(connect_string(str1, str2))
print()

#Challenges -

#K
for i in range(1, 6):
    for k in range(1, i + 1):
        print("*", end="")
    print()
print()

for i in range(7):
    j = 7 - 1 - i
    for k in range(7):
        if k == i or k == j:
            print("*", end="")
        else:
            print(end=" ")
    print(" ")
print()

#M
def number_from_user():
    while True:
        try:
            return int(input("Please provide me with a whole number: "))
        except ValueError:
            print("That wasn't a number, try again")

def digits_sum():
    numbers = []
    user_n = number_from_user()
    user_n2 = user_n
    while user_n >= 10:
        numbers.append(int(user_n % 10))
        user_n = user_n // 10
    numbers.append(user_n)
    numbers.reverse()
    numbers_sum = sum(numbers)
    summary_of_numbers_string = f"{numbers[0]}"
    for i  in range(1, len(numbers)):
        summary_of_numbers_string += f"+{numbers[i]}"
    print(f"The summary of all the digits in the number {user_n2} is: {numbers_sum}\n{summary_of_numbers_string} = {numbers_sum}")

digits_sum()