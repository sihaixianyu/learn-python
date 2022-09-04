from typing import List


def calculate_smmoth(nums: List[int]):
    n = len(nums)
    dp = [0] * n
    dp[0] = 0

    for i in range(1, n):
        dp[i] = max(dp[i - 1], abs(nums[i] - nums[i - 1]))

    return dp[-1]


if __name__ == "__main__":
    nums = [1, 3, 4]
    print(calculate_smmoth(nums))
