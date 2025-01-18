# This program get the argument from user and checks the given string is a palindrome or not(reads the same backward as forward).


def is_palindrome(word):
    if word == word[::-1]:
        return f"{word} is palindrome"
    else:
        return f"{word} is not palindrome"


test_word = input("Please enter the string: ")
result = is_palindrome(test_word)
print(result)