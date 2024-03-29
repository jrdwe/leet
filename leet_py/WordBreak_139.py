

# runtime: O(n^2 * m)
# space:   O(n)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * len(s) + [True]
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if len(w) + i <= len(s) and s[i : len(w) + i] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]: 
                    break
                    
        return dp[0]
