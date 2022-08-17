#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

bool validMountainArray(int* arr, int arrSize);

int main() 
{
	// int nums[] = { 0, 2, 3, 4, 5, 2, 1, 0 };
	int nums[] = { 0, 3, 2, 1 };
	size_t n = sizeof(nums)/sizeof(nums[0]);

	printf("Boolean: %d\n", validMountainArray(nums, n));

	return 0;
}

bool validMountainArray(int* arr, int arrSize)
{
	if (arrSize < 3)
		return false;
	
	int i;
	for (i = 1; i < arrSize && arr[i - 1] < arr[i]; ++i)
		;

	if (i == 1 || i == arrSize || arr[i - 1] == arr[i])
		return false;

	for (++i; i < arrSize && arr[i - 1] > arr[i]; ++i)
		;

	return (i >= arrSize);
}
