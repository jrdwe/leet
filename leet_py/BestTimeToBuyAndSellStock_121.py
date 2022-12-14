
# runtime: O(n)
# space:   O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lmax, gmax = 0, -inf
        for i, v in enumerate(prices):
            if i + 1 == len(prices): break
            lmax = max(prices[i + 1] - prices[i], prices[i + 1] - prices[i] + lmax)
            if lmax > gmax: gmax = lmax

        return gmax if gmax > 0 else 0

    def maxProfit(self, prices: List[int]) -> int:

        profit, lowest = 0, inf
        for price in prices:
            if lowest > price:
                lowest = price
            
            if price - lowest > profit:
                profit = price - lowest

        return profit

