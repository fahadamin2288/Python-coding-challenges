# This program checks that the given string are unique character or not



def unique_frequency_checker(string):
    freq = {}
    for i in string:
        freq[i] = freq.get(i, 0) + 1
    unique_frequencies = set(freq.values())
    if len(unique_frequencies) <= 2:
        if len(unique_frequencies) == 1:
            return True
        else:
            freq_list = list(unique_frequencies)
            freq_1 = freq_list[0]
            freq_2 = freq_list[1]
            if abs(freq_2 - freq_1) == 1:
                return True
    return False


s = input("Please enter the string: ")
print(unique_frequency_checker(s))
