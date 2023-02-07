
# runtime: O(n * m)
# space  : O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols, rZero = len(matrix), len(matrix[0]), False

        # Denote Row/Col to be 0'd
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        rZero = True

        # Every Row/Col aside from 0th
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # 0th Row Across
        if matrix[0][0] == 0:
            for row in range(rows):
                matrix[row][0] = 0

        # 0th Col Down
        if rZero:
            for col in range(cols):
                matrix[0][col] = 0
