
# runtime: O(n)
# space:   O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        levels, queue = [], deque([root])
        while queue:
            level = []
            child = []

            while queue:
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)

            queue.extend(child)
            levels.append(level)

        return [level[-1] for level in levels]
