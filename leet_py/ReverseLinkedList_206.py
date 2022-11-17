
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
 
# runtime: O(n)
# space:   O(1)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # None -> [] -> [] ->
        # None <- []    [] -> 
        # None <- [] <- [] -> 
        
        prev, node = None, head
        while node:
            node.next, node, prev = prev, node.next, node

        return prev


