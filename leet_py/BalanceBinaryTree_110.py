
# runtime: O(n)
# space:   O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(root):
            # check for valid node
            if root is None: return 0

            # recurse deeper down the tree
            left, right = helper(root.left), helper(root.right)

            # check balanced (if not return -1)
            if left < 0 or right < 0 or abs(left - right) > 1: return -1

            # compute the height for given node
            return max(left, right) + 1

        return helper(root) >= 0
