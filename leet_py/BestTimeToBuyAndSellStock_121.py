
# runtime: O(n)
# space:   O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest, profit = inf, 0
        for price in prices:
            lowest = min(price, lowest)
            profit = max(profit, price - lowest)

        return profit

