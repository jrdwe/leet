#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct ListNode 
{
  int val;
  struct ListNode *next;
};

/** @brief Given the heads of two sorted singly LL
 *         merge the two together. 
 *          
 *  @return New head of the LL
 */  
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
  if (!list1) { return list2; }
  if (!list2) { return list1; }

  struct ListNode *ptr;

  if (list1->val < list2->val) {
    ptr = list1;
    ptr->next = mergeTwoLists(list1->next, list2);
    return ptr;
  } else {
    ptr = list2;
    ptr->next = mergeTwoLists(list1, list2->next);
    return ptr;
  }
}
