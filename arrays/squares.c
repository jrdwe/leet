#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int* sortedSquares(int* nums, int numsSize, int* returnSize);
void printArray(int* nums, int numsSize);

int main()
{
	int nums[] = { -4, -1, 0, 3, 10 };
	size_t n = sizeof(nums)/sizeof(nums[0]);

	int len;
	int* arr = sortedSquares(nums, n, &len);

	printArray(arr, len);

	return 0;
}

void printArray(int* nums, int numsSize)
{
	printf("[ ");
	for (int i = 0; i < numsSize; ++i)
	{
		printf("%d ", nums[i]);
	}
	printf("] \n");
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
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

