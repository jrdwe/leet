
# runtime: O(kn^k)
# space  : O(n)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        out = []
        def helper(i, s):
            if len(s) == k:
                out.append(s[:])
                return

            for j in range(i, n + 1):
                s.append(j)
                helper(j + 1, s)
                s.pop()

        helper(1, [])
        return out

