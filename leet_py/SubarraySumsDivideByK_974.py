
# runtime: O(n)
# space  : O(n)

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        array, count    = [0 for value in range(k)], 0
        array[0]        = 1

        prefixsum = [nums[0]]
        for i in range(1, len(nums)):
            prefixsum.append(prefixsum[i - 1] + nums[i])

        for num in prefixsum:
            count               += array[num % k]
            array[num % k]      += 1

        return count
