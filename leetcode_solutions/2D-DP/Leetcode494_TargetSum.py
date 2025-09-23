from collections import defaultdict
def findTargetSum(self, nums: list[int], target: int) -> int:
    dp = defaultdict(int)
    dp[0]=1
    for num in nums:
        next_dp = defaultdict(int)
        for total, cnt in dp.items():
            next_dp[total + num] += cnt
            next_dp[total - num] += cnt
        dp = next_dp
    return dp[target]

# Time: O(N*S) where N is the length of nums and S is the sum of nums
# Space: O(S) where S is the sum of nums

