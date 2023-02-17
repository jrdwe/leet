
# runtime: O(n)
# space:   O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1

        # O(n) Two Pointer
        output, left, seen = 0, 0, {}
        for right, val in enumerate(s):
            if val in seen:
                left = max(left, seen[val] + 1)
            output = max(output, (right - left) + 1)
            seen[val] = right
        

        return output 
