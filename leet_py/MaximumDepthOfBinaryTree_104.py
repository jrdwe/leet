
# runtime: O(n)
# space;   O(1)

def maxDepth(self, root: TreeNode) -> int:

    def helper(root: TreeNode, val: int):
        if (root != None):
            val += 1
            return max(helper(root.left, val), helper(root.right, val))
        return val            

    return helper(root, 0)
