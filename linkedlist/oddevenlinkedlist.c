#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct ListNode 
{
  int val;
  struct ListNode *next;
};

/** @brief Given the heads of a singly LL
 *         Group all nodes with odd indices together
 *         followed by all nodes with even indices.
 *  
 *  @return New head of the LL
 */  
struct ListNode* oddEvenList(struct ListNode* head){
  if (!head) { return NULL; }

  struct ListNode *o = head, *e = head->next;
  struct ListNode *ehead = e;

  while (o->next && e->next) {
    o->next = o->next->next;
    e->next = e->next->next;
    o = o->next;
    e = e->next;
  }

  o->next = ehead;
  return head;
}
