
# runtime: O(2^n)
# space  : O(n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        out = []
        def helper(i, s):
            if i == len(nums):
                out.append(s[:])
            else:
                helper(i + 1, s)
                s.append(nums[i])
                helper(i + 1, s)
                s.pop()

        helper(0, [])
        return out
