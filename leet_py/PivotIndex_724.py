
# runtime: O(n)
# space: O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # find left and right sum
        lsum = 0
        rsum = sum(nums)

        # loop over all nums and compare
        for idx, val in enumerate(nums):
            rsum -= val
            if lsum == rsum:
                return idx
            lsum += val

        return -1
