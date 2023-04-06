
# runtime: O(n^2)
# space  : O(n)

class Solution:
    def longestPalindrome(self, s: str) -> str:

        cnt, out = -1, ""
        for i in range(len(s)):
            l, h = i, i
            while l >= 0 and h < len(s) and s[l] == s[h]:
                if h - l + 1 > cnt:
                    out, cnt = s[l:h + 1], h - l + 1
                l -= 1
                h += 1

            l, h = i, i + 1
            while l >= 0 and h < len(s) and s[l] == s[h]:
                if h - l + 1 > cnt:
                    out, cnt = s[l:h + 1], h - l + 1
                l -= 1
                h += 1

        return out
