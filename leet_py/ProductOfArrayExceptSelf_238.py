
# runtime: O(n)
# space  : O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:    return []

        # Output set-up
        output = len(nums) * [0]
        output[0] = 1

        # Prefix Product
        for i in range(1, len(nums)):
            output[i] = nums[i - 1] * output[i - 1]

        # Suffix Product
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix     = suffix * nums[i]

        return output
