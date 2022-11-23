
# recursive
# runtime: O(log n)
# space: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        mid = len(nums) // 2

        if len(nums) == 1:
            return mid if nums[mid] == target else -1
        elif nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return mid + self.search(nums[mid:], target) if self.search(nums[mid:], target) != -1 else -1
        elif nums[mid] > target:
            return self.search(nums[:mid], target)

# iterative
# runtime: O(log n)
# space: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low, high = 0, len(nums) - 1
        while high >= low:
            mid = (low + high) // 2
            if nums[mid] == target: return mid
            if nums[mid] <  target: low  = mid + 1
            if nums[mid] >  target: high = mid - 1

        return -1
