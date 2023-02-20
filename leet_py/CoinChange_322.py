
# runtime: O(n)
# space  : O(n)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        v, q = set(), deque([(amount, 0)])
        while q:
            curr, count = q.popleft()

            if curr == 0:
                return count

            for coin in coins:
                calc    = curr - coin
                if calc in v or calc < 0: continue
                q.append((calc, count + 1))
                v.add(calc)

        return -1
