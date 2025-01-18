# This python program working is check if Ransom Note Can Be Constructed from Magazine


def can_construct(ransomNote, magazine):
    magazine_count = {}
    for char in magazine:
        magazine_count[char] = magazine_count.get(char, 0) + 1
    for char in ransomNote:
        if char not in magazine_count or magazine_count[char] == 0:
            return False
        magazine_count[char] -= 1

    return True


a = "ab"
b = "aab"
print(can_construct(a, b))
