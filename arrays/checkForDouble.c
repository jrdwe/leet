#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

bool checkIfExist(int* arr, int arrSize);

int main() 
{
	int nums[] = { -2, 0, 10, -19, 4, 6, -8 };
	size_t n = sizeof(nums)/sizeof(nums[0]);

	printf("Boolean: %d\n", checkIfExist(nums, n));

	return 0;
}

bool checkIfExist(int* arr, int arrSize)
{
	for (int i = 0; i < arrSize; ++i)
	{
		for (int j = 0; j < arrSize; ++j)
			if (i != j && arr[i] * 2 == arr[j])
				return true;
	}

	return false;
}
