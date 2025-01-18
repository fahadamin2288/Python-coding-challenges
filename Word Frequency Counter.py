"""
This function counts the frequency of each word in a given sentence, and returns a dictionary where the keys are the
words and the values are the counts of how many times each word appears.
"""


def word_count(string):
    words = string.split()
    word = {}
    for i in words:
        if i in word:
            word[i] += 1
        else:
            word[i] = 1
    return word


stp = input("Please enter the sentence: ").lower()
result = word_count(stp)
print(result)