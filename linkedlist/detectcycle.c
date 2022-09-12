#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct ListNode 
{
	int val;
	struct ListNode *next;
};

/** @brief given the head of the LL, determine  
 *				 where the cycle begins.
 * 
 *  @return node of start of cycle 
 */  
struct ListNode*
detectCycle(struct ListNode *head)
{
	struct ListNode *s = head, *f = head;

	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;

		if (s == f) { break; }
	}
	
  if (!s || !f) { return NULL; }

  s = head;
  while (s != f)
  {
    f = f->next;
    s = s->next;
  }

	return s;
}

