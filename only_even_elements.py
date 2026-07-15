x = list(map(int,input().split()))

for i in x:
    if i % 2 != 0:
        print("False")
        break
else:
    print("True")