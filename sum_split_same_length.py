def split_equal_size_sum(nums):

    n = len(nums)
    total = sum(nums)

    if n % 2 != 0 or total % 2 != 0:
        return False

    target = total // 2

    dp = [set() for _ in range(n + 1)]
    dp[0].add(0)

    for num in nums:
        for k in range(n - 1, -1, -1):
            for s in list(dp[k]):
                dp[k + 1].add(s + num)

    return target in dp[n // 2]


nums = list(map(int, input().split()))
print(split_equal_size_sum(nums))