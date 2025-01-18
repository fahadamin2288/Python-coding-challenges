# This python program takes a list of numbers as input and returns the maximum number in the list.


def maximum(list1):
    max = list1[0]
    for i in list1:
        if i > max:
            max = i
    return max


lst = [33, 55, 45, 78]
print(maximum(lst))