
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# runtime: O(n)
# space:   O(n)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1): return l2
        if (not l2): return l1

        if (l1.val <= l2.val):
            node = l1
            node.next = self.mergeTwoLists(l1.next, l2)
            return node
        else:
            node = l2
            node.next = self.mergeTwoLists(l1, l2.next)
            return node

# runtime: O(n)
# space:   O(n)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = node = ListNode(-1)

        while l1 and l2:
            if (l1.val <= l2.val):
                node.next, l1 = l1, l1.next
            else: 
                node.next, l2 = l2, l2.next

            node = node.next
        
        node.next = l1 if l1 else l2
        return head.next
