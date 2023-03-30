

# runtime: O(n^2 * m)
# space:   O(n)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n, dp = len(s), [True] + [False] * (len(s) + 1)

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]
