
# runtime: O(n + m)
# space  : O(n + m)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        trow, brow = 0, len(matrix)
        lcol, rcol = 0, len(matrix[0])
        out        = []

        while trow < brow and lcol < rcol:
            # Right across
            for i in range(lcol, rcol):
                out.append(matrix[trow][i])
            trow += 1

            # Right Down
            for i in range(trow, brow):
                out.append(matrix[i][rcol - 1])
            rcol -= 1

            # Left Across
            for i in range(rcol - 1, lcol - 1, -1):
                if trow != brow:
                    out.append(matrix[brow - 1][i])
            brow -= 1

            # Left Up
            for i in range(brow - 1, trow - 1, -1):
                if lcol != rcol:
                    out.append(matrix[i][lcol])
            lcol += 1

        return out


