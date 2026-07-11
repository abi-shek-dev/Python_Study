n = int(input())
arr = list(map(int,input().split()))

max_profit = 0
min_price = arr[0]

for i in range(1,n):
    if arr[i] < min_price:
        min_price = arr[i]

    else:
        max_profit = max(max_profit, arr[i] - min_price)

print(max_profit)