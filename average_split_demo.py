def average_split(arr):

    total = sum(arr)
    n = len(arr)

    dp = [set() for _ in range(n + 1)]
    dp[0].add(0)

    for num in arr:
        
        for k in range(n - 1, -1, -1):
            
            for s in list(dp[k]):
                
                dp[k+1].add(num+s)
                
    for k in range(1,n):
        
        if total % k == 0:
            target = total // k
            
            if target in dp[k]:
                return True
            
    return False

arr = list(map(int,input().split()))
print(average_split(arr))