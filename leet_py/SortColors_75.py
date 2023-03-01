
# runtime: O(n)
# space  : O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        arr = [0, 0, 0]
        for i in nums:
            arr[i] += 1

        off = 0
        for i, n in enumerate(arr):
            for j in range(n):
                nums[j + off] = i
            off += n
