
# runtime: O(n)
# space:   O(n)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        kp = {}
        for item in s:
            if item not in kp:
                kp[item] = 1
            else:
                kp[item] += 1
            
        dups = 0
        for key in kp:
            if kp[key] // 2 > 0:
                dups += kp[key] // 2

        return (dups * 2) if len(s) == (dups * 2) else (dups * 2) + 1
