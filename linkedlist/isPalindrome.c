#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct ListNode 
{
  int val;
  struct ListNode *next;
};

/** @brief Given the head of a singly LL
 *         return if it's a palindrome 
 *           
 *  @return Returns Boolean
 */  
bool isPalindrome(struct ListNode* head){
  // Find the middle of the linked-list
  struct ListNode *mid = head, *fast = head->next;
  while (fast && fast->next) {
    mid = mid->next;
    fast = fast->next->next;
  }

  // Reverse the second half of the linked-list
  struct ListNode *prior = NULL;
  while (mid) {
    struct ListNode *tmp = mid->next;
    mid->next = prior;
    prior = mid;
    mid = tmp;
  }

  // Compare your two halves
  while (prior && head) {
    if (prior->val != head->val) { return false; }
    prior = prior->next;
    head = head->next;
  }

  return true;
}
