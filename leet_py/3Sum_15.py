
# runtime: O(n^2)
# space:   O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = []
        # sorting is critical
        nums.sort()

        for i, v in enumerate(nums):
            # skip duplicate values
            if i > 0 and nums[i - 1] == v:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = v + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left  += 1
                else:
                    output.append([v, nums[left], nums[right]])
                    # then shift left over
                    left  += 1
                    # ensure duplicates don't exist
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return output

