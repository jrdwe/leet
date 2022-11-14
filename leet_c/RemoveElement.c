#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* removeElement: given an array and integer value, remove the value in-place */
int removeElement(int* nums, int numsSize, int val)
{
	int i, c, b;

	for (i = 0, b = 0, c = 0; i < numsSize; ++i)
	{
		if (nums[i] != val)
		{
			nums[b++] = nums[i];
			++c;
		}
	}

	return c;
}
