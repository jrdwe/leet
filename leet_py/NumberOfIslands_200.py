
# runtime: O(n * m)
# space  : O(n * m)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(x, y, s, f):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == "0" or (x, y) in s:
                return 0

            f = 1 if f == 0 else 0

            s.add((x, y))
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + i, y + j, s, f)

            return f
        
        s, o = set(), 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                o += dfs(x, y, s, 0)

        return o
