#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int removeElement(int* nums, int numsSize, int val);

int main()
{
	int nums1[] = { 0, 1, 2, 2, 3, 0, 4, 2 };
	size_t n1 = sizeof(nums1)/sizeof(nums1[0]);
	int value = 2;

	removeElement(nums1, n1, value);

	for (int i = 0; i < n1; ++i)
		printf("%d\n", nums1[i]);	

	return 0;
}

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
