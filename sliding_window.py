n, k = map(int,input().split())
arr = list(map(int,input().split()))

max_len = 0
left = 0
total = 0

for right in range(n):
    total += arr[right]
    while total >= k :
        total -= arr[left]
        left += 1

    max_len = max(max_len, (right-left+1))

print(max_len)