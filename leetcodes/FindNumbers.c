#include <stdio.h>
#include <string.h>

#define LEN 1024

int findNumbers(int* nums, int numsSize)
{
	int i, c;
	char str[LEN];		

	for (i = 0, c = 0; i < numsSize; ++i)
	{
		sprintf(str, "%d", nums[i]);
		if (strlen(str) % 2 == 0)
			c++;
	}

	return c;
}
