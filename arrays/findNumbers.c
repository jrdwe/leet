#include <stdio.h>
#include <string.h>

#define LEN 1024

int findNumbers(int* nums, int numsSize);

int main()
{
	int nums[] = { 12, 345, 2, 6, 7696 };
	size_t n = sizeof(nums)/sizeof(nums[0]);

	printf("Value: %d\n", findNumbers(nums, n));

	return 0;
}

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
