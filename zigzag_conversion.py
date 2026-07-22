def zigzag(s , numrows):

    if numrows == 1 or numrows >= len(s):
        return s

    rows = [""] * numrows

    direction = -1
    current_row = 0

    for ch in s:
        rows[current_row] += ch

        if current_row == 0 or current_row == numrows - 1:
            direction *= -1

        current_row += direction

    return "".join(rows)

s = input()
numrows = int(input())
print(zigzag(s,numrows))