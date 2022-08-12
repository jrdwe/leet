#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n);

int main()
{
	int nums1[] = { 1, 2, 3, 0, 0, 0 };
	int nums2[] = { 2, 5, 6 };
	size_t n1 = sizeof(nums1)/sizeof(nums1[0]);
	size_t n2 = sizeof(nums2)/sizeof(nums2[0]);

	merge(nums1, n1, 3, nums2, n2, 3);

	for (int i = 0; i < n1; ++i)
		printf("%d\n", nums1[i]);	

	return 0;
}

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
