#include <stdlib.h>
#include <stdio.h>

// Time Complexity : O(nlogn)
// Space Complexity : O(n)

// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r)
{
    // Your code here
    // get sizes for subarrays
    int n1 = m - l + 1;
    int n2 = r - m;

    // Create sub arrays of above sizes
    int *arr1 = new int(n1);
    int *arr2 = new int(n2);

    // Copy data to sub arrays
    for (int i = 0; i < n1; ++i) arr1[i] = arr[l + i];
    for (int j = 0; j < n2; ++j) arr2[j] = arr[m + 1 + j];

    int a = 0, b = 0, c = l;

    // Merge
    while (a < n1 && b < n2)
    {
        if (arr1[a] <= arr2[b]) arr[c++] = arr1[a++];
        else arr[c++] = arr2[b++];
    }

    // Copy arr1[] remaining elements
    while (a < n1) arr[c++] = arr1[a++];

    // Copy arr2[] remaining elements
    while (b < n2) arr[c++] = arr2[b++];
}

/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
    // Your code here
    if (l < r)
    {
        // get the midpoint
        int m = l + (r - l) / 2;

        // Sort first half
        mergeSort(arr, l, m);
        // Sort second half
        mergeSort(arr, m + 1, r);
        // finally merge
        merge(arr, l, m, r);
    }
}

/* UTILITY FUNCTIONS */
/* Function to print an array */
void printArray(int A[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}

/* Driver program to test above functions */
int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr) / sizeof(arr[0]);

    printf("Given array is \n");
    printArray(arr, arr_size);

    mergeSort(arr, 0, arr_size - 1);

    printf("\nSorted array is \n");
    printArray(arr, arr_size);
    return 0;
}