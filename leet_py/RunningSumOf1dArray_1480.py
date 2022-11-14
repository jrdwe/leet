
# runtime: O(n)
# space: O(n)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = []
        t = 0
        for n in nums:
            t += n
            l.append(t)

        return l

