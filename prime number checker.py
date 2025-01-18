# This python program checks that the given number is prime or not

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


num = int(input("Please enter the number: "))
print(is_prime(num))