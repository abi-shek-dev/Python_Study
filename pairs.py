n, k = map(int,input().split())
arr = list(map(int,input().split()))

s = set(arr)
count = 0

for num in arr:
    if num + k in s:
        count += 1
        