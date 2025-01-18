# This python program calculate the prices of things.


def calculator():
    Sum = 0
    while True:
        thing_price = input("Enter the prices or press enter to quit: \n")
        if thing_price != ("Enter".lower()):
            Sum = Sum + int(thing_price)
            print(f"Order total so far {Sum}")

        else:
            print(f"Your total bill is {Sum}")
            break


calculator()
