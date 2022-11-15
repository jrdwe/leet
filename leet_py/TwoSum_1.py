
# runtime: O(n)
# space:   O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        kp = {}
        for i, val in enumerate(nums):
            n = target - val

            if n not in kp:
                kp[val] = i
            else:
                return [kp[n], i]

