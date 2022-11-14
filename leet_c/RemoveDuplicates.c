#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* removeDuplicates: given an array and integer value, remove 
 * all values such that each value only appears once from the sorted array */
int removeDuplicates(int* nums, int numsSize)
{
	int c, i;

	for (c = 0, i = 1; i < numsSize; ++i)
	{
		if (nums[i] != nums[c])
			nums[++c] = nums[i];
	}

	return c + 1;
}
