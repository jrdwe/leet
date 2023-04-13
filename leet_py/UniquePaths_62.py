
# runtime: O(nm)
# space  : O(nm)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        arr = [[0] * m for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i == n - 1 or j == m - 1:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i + 1][j] + arr[i][j + 1]

        return arr[0][0]
