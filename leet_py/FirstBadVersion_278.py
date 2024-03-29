
# runtime: O(log n)
# space:   O(1)

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# class Solution:
#     def firstBadVersion(self, n: int) -> int:
# 
#         l, h = 1, n
#         while (l < h):
#             mid = (l + h) // 2
#             calc = isBadVersion(mid)
#             if (calc == True):  h = mid
#             if (calc == False): l = mid + 1
# 
#         return h

class Solution:
    def firstBadVersion(self, n: int) -> int:

        x, b = -1, n
        while b >= 1:
            while (not isBadVersion(x + b)):
                x += b
            b //= 2

        return x + 1
