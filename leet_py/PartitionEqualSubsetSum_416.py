
# runtime: O(n^2)
# space:   O(n)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        targ = sum(nums) // 2
        dp   = [True] + [False] * (targ)

        for num in nums:
            for j in range(targ, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[targ]
