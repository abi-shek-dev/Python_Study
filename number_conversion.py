n = int(input())

print("Binary:", bin(n)[2:])
print("Octal:", oct(n)[2:])
print("Hexadecimal:", hex(n)[2:])

x = bin(n)
y = oct(n)
z = hex(n)

print(int(x, 2))
print(int(y,8))
print(int(z,16))