arr = list(map(int, input().split()))
n = len(arr)

for i in range(n):
    for j in range(i + 1, n + 1):
        print(*arr[i:j])