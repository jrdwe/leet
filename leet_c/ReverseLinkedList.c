#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct ListNode 
{
  int val;
  struct ListNode *next;
};

/** @brief Given the heads of a singly LL reverse it
 *  
 *  @return the new head of the list
 */  
struct ListNode* reverseList(struct ListNode* head){
  struct ListNode *prior = NULL;
  while (head) {
    struct ListNode *temp = head->next;
    head->next = prior;
    prior = head;
    head = temp;
  }

  return prior;
}

