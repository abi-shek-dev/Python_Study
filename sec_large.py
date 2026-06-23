from collections import Counter

arr = ["aaa", "aaa", "bbb", "ccc", "ddd", "aaa", "bbb"]

freq = Counter(arr)

first = second = 0
first_str = second_str = ""

for s, count in freq.items():
    if count > first:
        second, second_str = first, first_str
        first, first_str = count, s
    elif count > second:
        second, second_str = count, s

print(second_str)