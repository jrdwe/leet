
# runtime: O(n)
# space:   O(1)

# kadene's algo

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        count, largest = 0, -inf
        for number in nums:
            count   = max(number, number + count)
            largest = max(count, largest)

        return largest

