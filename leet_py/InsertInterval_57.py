
# runtime: O(n)
# space:   O(n)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        i, l, o = 0, len(intervals), []
        while i < l:
            if newInterval[0] > intervals[i][1]:
                o.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                o.append(newInterval)
                return o + intervals[i:]
            else:
                newInterval = [min(intervals[i][0], newInterval[0]),
                               max(intervals[i][1], newInterval[1])]
            i += 1

        o.append(newInterval)
        return o
