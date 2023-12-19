// Time Complexity : O(nlogn)
// Space Complexity : O(n) for array  + O(logn) auxillary stack space for recurssion
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :
#include <stdlib.h>
#include <stdio.h>

// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r)
{
    int nl = m - l + 1;
    int nr = r - m;

    int arrL[nl], arrR[nr];
    // populate left sub array
    for (int i = 0; i < nl; i++)
    {
        arrL[i] = arr[l + i];
    }
    // populate right sub array
    for (int j = 0; j < nr; j++)
    {
        arrR[j] = arr[m + 1 + j];
    }
    // i leftarr index //j right arr index //k main array index
    int i = 0, j = 0, k = l;

    while (i < nl && j < nr)
    {
        if (arrL[i] <=arrR[j])
        {
            arr[k] = arrL[i];
            i++;
        }
        else
        {
            arr[k] = arrR[j];
            j++;
        }
        k++;
    }
    while (i < nl)
    {
        arr[k] = arrL[i];
        k++;
        i++;
    }
    while (j < nr)
    {
        arr[k] = arrR[j];
        k++;
        j++;
    }
}

/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
    if (l < r)
    {
        int mid = l + (r - l) / 2;
        mergeSort(arr, l, mid);//t(n/2)
        mergeSort(arr, mid + 1, r); // t(n/2)
        merge(arr, l, mid, r); //O(n);
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