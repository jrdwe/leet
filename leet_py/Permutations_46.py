
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        o, l, s = [], len(nums), [False] * len(nums)
        def helper(n):
            if len(n) == l:
                o.append(n[:])

            for i in range(l):
                if (s[i]): continue
                s[i] = True
                n.append(nums[i])
                helper(n)
                s[i] = False
                n.pop()

        helper([])
        return o
