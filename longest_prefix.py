x = input()

string = ""

for i in range(len(x) - 1, 0, -1):
    if x[:i] == x[-i:]:
        string = x[:i]
        break

print(string)