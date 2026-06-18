from collections import Counter

a = "anagram"
b = "nagaram"

if Counter(a) == Counter(b):
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")