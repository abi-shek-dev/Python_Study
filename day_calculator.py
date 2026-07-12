day = input().lower()
n = int(input())

days = {
    "sun": 0,
    "mon": 6,
    "tue": 5,
    "wed": 4,
    "thu": 3,
    "fri": 2,
    "sat": 1
}

first = days[day]

if first > n:
    print(0)
else:
    print((n - first) // 7 + 1)