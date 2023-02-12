
# runtime: O(n)
# space  : O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        a, c = None, 0
        for n in nums:
            if c == 0:
                a = n
            c += 1 if n == a else -1

        return a
