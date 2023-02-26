
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# runtime: O(n)
# space  : O(n)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        paths = []
        def pathFinder(node, arr):
            if node == None:
                return

            arr.append(node)
            if node == p or node == q:
                paths.append(arr[:])

            pathFinder(node.left, arr)
            pathFinder(node.right, arr)
            arr.pop()

        pathFinder(root, [])

        l = min(len(paths[0]), len(paths[1]))
        for i in range(l - 1, -1, -1):
            if paths[0][i] == paths[1][i]:
                return paths[0][i]

# runtime: O(n)
# space  : O(h)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root is None:
            return None

        if root == p or root == q:
            return root

        left_v  = self.lowestCommonAncestor(root.left , p, q)
        right_v = self.lowestCommonAncestor(root.right, p, q)

        if left_v and right_v:
            return root

        return left_v if left_v != None else right_v

