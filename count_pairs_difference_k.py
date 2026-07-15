arr = list(map(int, input().split()))
k = int(input())

seen = set()
count = 0

for num in arr:
    if num - k in seen:
        count += 1
    if num + k in seen:
        count += 1
    seen.add(num)

print(count)