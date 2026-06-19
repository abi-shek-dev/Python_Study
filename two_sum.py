x = list(map(int, input().split()))
target = int(input())

seen = dict()

for i in range(len(x)):
    
    val = target - x[i]
    
    if val in seen:
        print(i, seen[val])
        break
    else:
        seen[x[i]] = i
    
else:
    print("No matches")