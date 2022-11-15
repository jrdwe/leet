
# runtime: O(n)
# space:   O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        if len(s) == 0:     return True

        j, m = 0, len(s)
        for i in range(len(t)):
            if s[j] == t[i]:
                j += 1
            if j >= m:
                break
                
        return j == m

