
# runtime: O(n)
# space:   O(1)

# kadene's algo

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lmax, gmax = 0, -inf
        for idx, val in enumerate(nums):
            lmax = max(nums[idx], nums[idx] + lmax)
            if (lmax > gmax): gmax = lmax
        return gmax
