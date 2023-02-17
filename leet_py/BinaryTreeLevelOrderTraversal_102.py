
# runtime: O(n)
# space:   O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
            
        levels = []
        loop   = [root]
        
        while loop:
            level = []  # stores all values for current level
            seen  = []  # stores the next levels nodes
            while loop:
                curr = loop.pop(0)
                level.append(curr.val)
                if curr.left:
                    seen.append(curr.left)
                if curr.right:
                    seen.append(curr.right)
            levels.append(level)
            loop = seen

        return levels
