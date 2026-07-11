def findmismatch(n,arr):
    if arr[0] == arr[-1]:
        return 0
    else:
        count = 0
        for i in range(1,n):
            if arr[i] != arr[0]:
                count+=1
        return count

n = int(input())
arr = list(map(int,input().split()))

print(findmismatch(n,arr))