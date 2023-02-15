
# runtime: O(max(n,m))
# space  : O(n)

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        o, i, j, c = "", len(a) - 1, len(b) - 1, 0
        while i > -1 or j > -1:
            s = c
            if i >= 0: s += ord(a[i]) - ord('0')
            if j >= 0: s += ord(b[j]) - ord('0')
            i, j = i - 1, j - 1
            c = 1 if s > 1 else 0
            o += str(s % 2)

        if c == 1:  o += str(c)
        return o[::-1]
