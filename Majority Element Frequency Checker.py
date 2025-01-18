""""
This function checks how many times a specified majority element (in this case, 3) appears in the given list,and returns
the count along with a message indicating how many times the element appears
"""


def majority_element_check(list):
    count = 0
    majority_element = 3
    for i in list:
        if i == majority_element:
            count = count + 1
    return f"{majority_element} is {count} time in given input"


lst = [2, 3, 5, 5, 3, 7, 8]
print(majority_element_check(lst))