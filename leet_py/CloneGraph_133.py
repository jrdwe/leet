
# runtime: O(n)
# space:   O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        seen = {}
        def clone(node):
            if node in seen:
                return seen[node]

            # create copy
            copy = Node(node.val)

            # add copy
            seen[node] = copy

            # add neighbors
            for connection in node.neighbors:
                copy.neighbors.append(clone(connection))

            # return clone
            return copy

        return clone(node) if node else None
