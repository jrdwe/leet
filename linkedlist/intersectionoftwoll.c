#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct ListNode 
{
  int val;
  struct ListNode *next;
};


/** @brief Given a node of the LL
 *         find the count of nodes till
 *         the end
 *
 *  @return integer
 */
int 
listLength (struct ListNode *head) {
  int len = 0;

  for (; head; len++)
    head = head->next;

  return len;
}

/** @brief Given the heads of two singly LL
 *         return the node at which the two intersect.
 *  
 *  @return node of intersect
 */  
struct ListNode*
getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
  if (headA == NULL || headB == NULL) { return NULL; }
  if (headA == headB) { return headA; }

  struct ListNode *tA = headA, *tB = headB;
  int len_a = listLength(headA), len_b = listLength(headB);
  int diff = abs(len_a - len_b);

  if (len_a > len_b) {
    for (int i = 0; i < diff; i++)
      tA = tA->next;
  } else {
    for (int i = 0; i < diff; i++)
      tB = tB->next;        
  }

  while (tA && tB) {
    if (tA == tB)
      return tA;

    tB = tB->next;
    tA = tA->next;
  }

  return NULL;
}

