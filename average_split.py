def split_same_average(nums):

    n = len(nums)
    total = sum(nums)
    print("Total Sum: ",total)

    dp = [set() for _ in range(n + 1)]
    dp[0].add(0)

    for num in nums:

        for k in range(n - 1, -1, -1):

            for s in list(dp[k]):
                dp[k + 1].add(s + num)

    for k in range(1, n):

        if (total * k) % n == 0:

            target = (total * k) // n

            if target in dp[k]:
                return True

    return False


nums = list(map(int, input().split()))
print(split_same_average(nums))