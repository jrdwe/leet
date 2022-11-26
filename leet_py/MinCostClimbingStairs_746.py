
# runtime: O(n)
# space:   O(1)

# Iterate backwards through list
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.insert(0, 0)
        v1, v2 = cost[len(cost) - 2], cost[len(cost) - 1]
        for i in range(len(cost) - 3, -1, -1):
            v2, v1 = v1, min(v1 + cost[i], v2 + cost[i])

        return min(v1, v2)

# Iterate forward through list
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        v1, v2 = cost[:2]
        for i in range(2, len(cost)):
            v1, v2 = v2, min(v1, v2) + cost[i]

        return min(v1, v2)
        
