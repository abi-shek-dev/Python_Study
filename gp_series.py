class Solution:
    # Function to calculate GP sum
    def sumOfGP(self, a, r, n):
        # If ratio is 1
        if r == 1:
            return a * n

        # Use GP formula for r ≠ 1
        return a * (r ** n - 1) / (r - 1)

# Sample input values
a = 1
r = 0.5
n = 3

# Creating object and calling method
obj = Solution()
result = obj.sumOfGP(a, r, n)

# Printing result
print(result)