#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

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
