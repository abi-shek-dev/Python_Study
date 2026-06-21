x = int(input())

result = 0

while x > 0:
    d = x % 10
    result = result * 10 + d
    x //= 10
    
print( result)