#include <stdio.h>

int findMaxConsecutiveOnes(int* nums, int numsSize)
{
	int i, curr, longest;	

	for (i = 0, curr = 0, longest = 0; i < numsSize; ++i)
	{
		if (nums[i] != 1)
			curr = 0;
		else
			if (curr++ >= longest)
				longest = curr;
	}

	return longest;
}
