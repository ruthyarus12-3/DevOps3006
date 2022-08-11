print("------- A -------")
from random import randint

x = 3
y = 6
if x > y:
    print("BIG")
else:
    print("small")

print("------- B -------")
for i in range(5):
    print(i)

print("------- C -------")
value = randint(1, 4)
if value == 1:
    print("summer")
elif value == 2:
    print("winter")
elif value == 3:
    print("fall")
elif value == 4:
    print("spring")

print("------- D -------")
# 1. 10 times
# 2. 10

print("------- E -------")
my_age = 32
print(my_age)
my_name = "Ruth"
first_letter_of_my_name = my_name[0]
print(first_letter_of_my_name)
shekel_dollar_currency = 3.49
print(shekel_dollar_currency)
flew_abroad = True
print(flew_abroad)
my_apartment_number = 8
print(my_apartment_number)
age_currency = my_age + shekel_dollar_currency
print(age_currency)

print("------- F -------")
# phone_number = input('What is your phone number?\n')
# print(f"phone number {phone_number}")

print("------- G -------")


def printHello():
    print("hello")


def calculate():
    print(5 + 3.2)


print("------- H -------")


def print_my_name(name: str):
    print(name)


def divide_by_two(num):
    print(num / 2)


print("------- I -------")


def add(num1, num2):
    print(num1 + num2)


def spaced_strings(str1, str2):
    print(f"{str1} {str2}")


print("------- K -------")
for row in range(1, 6):
    print(row * "#")

print("------- L -------")


print("------- M -------")


def get_a_number():
    number = input("Insert a number\n")
    return number


def sum_digits(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sum_digits(num // 10)


print(sum_digits(int(get_a_number())))
