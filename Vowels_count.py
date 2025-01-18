# This program provides the frequency of vowels letter from the given string



def count_vowels(input_string):
    vowel_count = 0
    for char in input_string:
        if char.lower() in 'aeiou':
            vowel_count += 1
    return vowel_count


str = input("Please enter the string: ")
print(count_vowels(str))
