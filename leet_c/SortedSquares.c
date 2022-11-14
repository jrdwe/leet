#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/**
 * Note: The returned array must be malloc'd, assume caller calls free().
 * We assume that the array nums is sorted in non-decreasing order
 */
int* sortedSquares(int* nums, int numsSize, int* returnSize)
{
	int* arr = malloc(sizeof(int) * numsSize);
	int left = 0, right = numsSize - 1, counter = numsSize - 1;
	*returnSize = numsSize;

	while (left <= right)
	{
		if (abs(nums[left]) > abs(nums[right]))
		{
			arr[counter--] = pow(nums[left], 2);
			left++;
		} 
		else 
		{
			arr[counter--] = pow(nums[right], 2);
			right--;
		}
	}

	return arr; 
}

