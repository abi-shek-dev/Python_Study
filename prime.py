# Define the range boundaries
end = 5

print(f"Prime numbers between 1 and {end} are:")

for num in range(1, end + 1):
    # Prime numbers must be greater than 1
    if num > 1:
        # Check for factors up to the square root of the number
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break
        else:
            # Runs only if no factors were found
            print(num, end=" ")
