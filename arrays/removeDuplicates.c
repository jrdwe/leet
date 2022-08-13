#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int removeDuplicates(int* nums, int numsSize);

int main()
{
	int nums1[] = { 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 };
	// int nums1[] = { 1, 1, 2 };
	size_t n1 = sizeof(nums1)/sizeof(nums1[0]);

	removeDuplicates(nums1, n1);

	for (int i = 0; i < n1; ++i)
		printf("%d\n", nums1[i]);	

	return 0;
}

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
