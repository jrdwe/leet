#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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
