# This python program takes a number as input and returns "Even" if the number is even and "Odd" if it's odd.


def check_number(number):
    if number % 2 == 0:
        return f"{number} is the even number"
    else:
        return f"{number} is the odd number"


try:
    num = int(input("Enter the number: "))
    print(check_number(num))
except ValueError as e:
    print("Only integer are allowed")