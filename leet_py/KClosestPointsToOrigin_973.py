
# runtime: O(n * logk)
# space:   O(k)

# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
# 
#         return sorted(points, key = lambda x:x[0]**2 + x[1]**2)[:k]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for (x, y) in points:
            dist = -1 * (x**2 + y**2)
            if len(heap) == k:
                # pushes item on the heap, then pops and returns the smallest item from the heap
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [(x, y) for (dist, x, y) in heap]
