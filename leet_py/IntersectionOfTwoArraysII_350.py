
# runtime: O(n + m)
# space:   O(n)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # dict storing values & count for nums1
        d1 = {}
        for n in nums1:
            if n not in d1:
                d1[n] = 1
            else:
                d1[n] += 1   
        
        # generate final array 
        arr = []
        for n in nums2:
            if n not in d1.keys():
                continue
            elif d1[n] > 0:
                d1[n] -= 1
                arr.append(n)

        return arr
