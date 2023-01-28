
# runtime: O((4^n)/sqrt(n))
# space  : O((4^n)/sqrt(n))

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def helper(v, o, c, p = []):
            if o    : helper(v + "(", o - 1, c)
            if c > o: helper(v + ")", o, c - 1)
            if not c: p.append(v)

            return p


        return helper('', n, n)
