#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* merge sorted array: merge nums1 & nums2 into a single array in increasing order */ 
void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n)
{
	int i = m - 1;
	int j = n - 1;
	int c = n + m - 1;

	while (j >= 0)
	{
		if (i >= 0 && nums1[i] > nums2[j])
			nums1[c--] = nums1[i--];
		else
			nums1[c--] = nums2[j--];
	}
}
