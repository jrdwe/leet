
# runtime: O(n)
# space  : O(n)

class Solution:
    def __init__(self):
	    self.diameter = 0

    def depth(self, node):
        l = self.depth(node.left) if node.left else 0
        r = self.depth(node.right) if node.right else 0
        self.diameter = max(self.diameter, l + r)
        return 1 + max(l, r)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.diameter
