# This python program takes a list of numbers as input and returns the maximum and minimum number in the list.


def find_max_and_num(num):
    max = num[0]
    min = num[0]
    if (len(num)) > 1:
        for i in range(1, len(num)):
            if num[i] > max:
                max = num[i]
            if num[i] < min:
                min = num[i]
        return f"Maximum element is: {max}\nMinimum element is: {min}"
    else:
        return 0



list = [3, 5, 4, 1, 9]
list = [3]
print(find_max_and_num(list))
