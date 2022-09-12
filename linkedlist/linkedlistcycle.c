#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct ListNode 
{
	int val;
	struct ListNode *next;
};

/** @brief given the head of the LL, determine if 
 *				 there exists a cycle.
 * 
 *  @return true when linked-list has cycle 
 */  
bool
hasCycle(struct ListNode *head)
{
	if (!head || !head->next) { return false; }

	struct ListNode *s = head, *f = head;

	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;

		if (s == f) { return true; }
	}
	
	return false;
}

