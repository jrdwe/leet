
# runtime: O(n)
# space:   O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        arr = []
        def helper(root):
            if root:
                arr.append(root.val)
                for i in root.children:
                    helper(i)
        
        helper(root)
        return arr
