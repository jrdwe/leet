
# runtime: O(n)
# space:   O(1)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        output = []

        # iterate all items in interval
        for i in range(len(intervals)):

            # append newinterval first
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:]

            # append interval first
            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])

            # handle merge overlap
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        # ensures newInterval is included
        output.append(newInterval)

        # return final output array
        return output

