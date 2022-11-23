
# runtime: O(n)
# space:   O(1)

class Solution:
    def climbStairs(self, n: int) -> int:

        a, b = 1, 1
        for i in range(n - 1):
            b, a = a, a + b

        return a
