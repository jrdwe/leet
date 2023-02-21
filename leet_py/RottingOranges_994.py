
# runtime: O(n * m)
# space  : O(n * m)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        s, q, m  = set(), deque([]), 0
        row, col = range(len(grid)), range(len(grid[0]))

        for r in row:
            for c in col:
                if grid[r][c] == 2:
                    q.append((r, c, 0))

        while q:
            x, y, c = q.popleft()
            if x < 0 or len(grid) <= x or y < 0 or len(grid[0]) <= y or (x, y) in s or grid[x][y] == 0:
                continue

            s.add((x, y))
            grid[x][y] = 2
            m          = max(m, c)

            for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                q.append((x + a, y + b, c + 1))

        for r in row:
            for c in col:
                if grid[r][c] == 1:
                    return -1

        return m
