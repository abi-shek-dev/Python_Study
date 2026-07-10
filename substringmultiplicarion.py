s = input()

current_str = ""
current_number = 0
stack = []

for ch in s:

    if ch.isdigit():
        current_number = current_number * 10 + int(ch)

    elif ch == "[":
        stack.append((current_str, current_number))
        current_number = 0
        current_str = ""

    elif ch == "]":
        prev_str, num = stack.pop()
        current_str = prev_str + current_str * num

    else:
        current_str += ch

print(current_str)