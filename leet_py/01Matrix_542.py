
# runtime: O(n*m)
# space:   O(n*m)

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        def bfs(x, y, s, q):
            while q:
                i, j, d = q.popleft()
                for x, y in [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]:
                    if x < 0 or y < 0 or x >= len(mat) or y >= len(mat[0]) or (x, y) in s:
                        continue

                    if mat[x][y] == 1:
                        s.add((x, y))
                        mat[x][y] = d
                        q.append((x, y, d + 1))
            return mat
            
        s, q = set(), deque()
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if mat[x][y] == 0:
                    q.append((x, y, 1))

        return bfs(x, y, s, q)

