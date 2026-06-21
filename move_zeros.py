arr = list(map(int,input().split()))

counter = 0

result = []

for i in reversed(arr):
    if i == 0:
        counter += 1
        continue 
    else:
        result.append(i)
        
for i in range(counter):
    result.append(0)
    
print(*result)