
# runtime: O(nlogn)
# space  : O(1)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda l:l[0])
        i, c = 0, len(intervals)
        while i < c - 1:
            if intervals[i + 1][0] <= intervals[i][1]:
                intervals[i] = [min(intervals[i + 1][0], intervals[i][0]),
                                max(intervals[i + 1][1], intervals[i][1])]
                intervals.pop(i + 1)
                c -= 1
            else:
                i += 1

        return intervals
