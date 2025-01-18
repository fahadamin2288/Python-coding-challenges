# This python program calculate the factorial of given number.


def factorial_of_number(fact):
    factorial = 1
    if fact == 0:
        return "Factorial of 0 is 1"
    else:
        for i in range(1, x+1):
            factorial *= i

        return f"Factorial of {fact} is {factorial}."


x = int(input('Enter the number: '))
print(factorial_of_number(x))