
# This one's kinda slow... Use bottom one.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def maxDepth(root, level = 0):
            if root:
                level += 1
                return max(maxDepth(root.left, level), maxDepth(root.right, level))
            return level

        def traverseLevel(root, level):
            if root:
                if level == 1:
                    arr.append(root.val)
                elif level > 1:
                    traverseLevel(root.left,  level - 1)
                    traverseLevel(root.right, level - 1)

        ans = []
        depth = maxDepth(root)
        for level in range(1, depth + 1):
            arr = []
            traverseLevel(root, level)
            ans.append(arr)

        return ans

# runtime: O(n)
# space:   O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []
        loop   = [root]

        while len(loop):

            level = []  # stores all values for current level
            seen  = []  # stores the next levels nodes

            while len(loop):
                curr = loop.pop(0)
                level.append(curr.val)
                if curr.left:
                    seen.append(curr.left)
                if curr.right:
                    seen.append(curr.right)


            levels.append(level)
            loop = seen

        return levels

