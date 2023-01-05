
# runtime: O(n*m)
# space:   O(n*m)

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        row, col = len(mat), len(mat[0])
        queue = deque()

        for x in range(row):
            for y in range(col):
                if mat[x][y] == 0:
                    # tuple with coordinates and dist
                    queue.append((x, y, 1))

        return self.bfs(row, col, queue, mat)

    def bfs(self, row, col, queue, matrix):

        visited = set()
        while queue:
            x, y, dist = queue.popleft()
            for ax, ay in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= ax < row and 0 <= ay < col and (ax, ay) not in visited:
                    if matrix[ax][ay] == 1:
                        visited.add((ax, ay))
                        matrix[ax][ay] = dist
                        # add to queue and increase dist
                        queue.append((ax, ay, dist + 1))

        return matrix

