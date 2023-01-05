
# runtime: O(n)
# space:   O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        out, longest = [], 0
        for ch in s:
            if ch not in out:
                out.append(ch)
            else:
                out = out[out.index(ch) + 1:]
                out.append(ch)

            print(out)
            if len(out) > longest:
                longest = len(out)

        return longest
