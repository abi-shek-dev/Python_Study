s1 = input()
s2 = input()

ans = [ch for ch in s1 if ch not in s2]

print("".join(ans))