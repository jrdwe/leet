
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        o = []
        def helper(v, n, i):
            if v > target: return

            if v == target:
                o.append(n[:])
                return

            for j in range(i, len(candidates)):
                v += candidates[j]
                n.append(candidates[j])
                helper(v, n, j)
                n.pop()
                v -= candidates[j]

        helper(0, [], 0)
        return o
