
# runtime: O(n)
# space:   O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        # simple python solution
        # 
        # nums1[m:] = nums2
        # return nums1.sort()
        #

        # general solution
        i, j, l = m - 1, n - 1, m + n - 1
        while (j >= 0):
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[l] = nums1[i]
                i -= 1
            else:
                nums1[l] = nums2[j]
                j -= 1
            l -= 1
