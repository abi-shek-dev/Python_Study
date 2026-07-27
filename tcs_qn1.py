n = int(input())

mat = []
total = 0

for _ in range(n):
    arr = list(map(int,input().split()))
    mat.append(arr)
    total += sum(arr)

if total % 2 != 0:

    for i in range(n):
        mat[i] = mat[i][::-1]

    diagonal_sum = 0

    for i in range(n):
        diagonal_sum += mat[i][i]

else:

    for i in range(n//2):
        mat[i], mat[-(i+1)] = mat[-(i+1)], mat[i]

    diagonal_sum = 0

    for i in range(n):
        diagonal_sum += mat[i][i]

flattened_array = []

for i in mat:
    for j in i :
        flattened_array.append(j)

print(*flattened_array,diagonal_sum)