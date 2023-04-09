
# runtime: O(V + E) 
# space  : O(V + E) 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        m = { i:[] for i in range(numCourses) }
        for (x, y) in prerequisites:
            m[y].append(x)

        def dfs(n, s):
            if n in s: return False
            if m[n] == []: return True
            s.add(n)
            for ne in m[n]:
                if not dfs(ne, s): return False
            s.remove(n)
            m[n] = []
            return True

        for n in range(numCourses):
            if not dfs(n, set()): return False

        return True
