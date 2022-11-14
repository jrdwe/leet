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

/** @brief Given the heads of a singly LL
 *         and the value n. remove the nth from the end node
 *  
 *  @return head of the LL 
 */  
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
  if (!head) { return NULL; }

  struct ListNode *temp = head;
  int len = listLength(head); 
  int step = 1; 

  if ((len - n) == 0) { return temp->next; }

  while (step < (len - n)) {
    temp = temp->next;
    step++;
  }

  if (temp->next) {
    (temp->next->next) ? (temp->next = temp->next->next) 
                       : (temp->next = NULL);
  } 

  return head;
}
