#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void duplicateZeros(int* nums, int numsSize);

int main()
{
	int nums[] = { 12, 0, 2, 6, 7696 };
	size_t n = sizeof(nums)/sizeof(nums[0]);

	duplicateZeros(nums, n);

	/*
	for (int i = 0; i < n; ++i)
		printf("%d\n", nums[i]);	
	*/

	return 0;
}

/* duplicateZeros: given a fixed-len array, duplicate each occurrence of zero */
void duplicateZeros(int* nums, int numsSize)
{
	int i, j;
	int* arr = malloc(sizeof(int) * numsSize);	

	for (i = j = 0; j < numsSize && i < numsSize; ++i)
	{
		if (nums[i] == 0)
		{
			arr[j++] = nums[i];
			if (j < numsSize)
				arr[j++] = 0;
		}
		else 
		{
			arr[j++] = nums[i];
		}
	}

	memcpy(nums, arr, (sizeof(int) * numsSize));
	free(arr);
}
