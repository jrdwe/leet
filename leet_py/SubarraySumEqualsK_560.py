
# runtime: O(n)
# space  : O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        total, rolling, kp = 0, 0, {0 : 1}
        for number in nums:
            rolling     += number
            total       += kp.get(rolling - k, 0)
            kp[rolling]  = 1 + kp.get(rolling, 0)

        return total
