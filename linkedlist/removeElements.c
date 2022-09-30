#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct ListNode 
{
  int val;
  struct ListNode *next;
};

/** @brief Given the head of a singly linked-list
 *         and a value, n. Remove all nodes with n.
 *  
 *  @return the new head of the list
 */  
struct ListNode* removeElements(struct ListNode* head, int val){
  while (head && head->val == val) 
    head = head->next;

  struct ListNode *curr = head;
  while (curr) {
    if (curr->next && curr->next->val == val) {
      curr->next = curr->next->next;
    } else {
      curr = curr->next;
    }
  }

  return head;
}
