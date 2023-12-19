// Time Complexity : O(NlogN)
        // logN to divide into halves, N for merging the halves  
// Space Complexity : O(N) + O(N) 
        // use of temp array while merging and recursion call stack

#include <stdlib.h>
#include <stdio.h>

// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r)
{
    // Your code here
    int arr_size = r - l + 1;

    // initialized the temp array to store the elements
    int temp[arr_size], tempIndex = 0;

    int firstIndex = l, secondIndex = m + 1;

    // copy elements till either of the indices reach the end
    while (firstIndex <= m && secondIndex <= r)
    {
        if (arr[firstIndex] <= arr[secondIndex])
            temp[tempIndex++] = arr[firstIndex++];

        else
            temp[tempIndex++] = arr[secondIndex++];
    }

    // copy left over elements in the first half
    while (firstIndex <= m)
        temp[tempIndex++] = arr[firstIndex++];

    // copy left over elements in the second half
    while (secondIndex <= r)
        temp[tempIndex++] = arr[secondIndex++];

    // copying the elements from temp array to original array
    for (int index = 0; index < tempIndex; index++)
        arr[index + l] = temp[index];
}

/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
    // Your code here
    if (l == r)
        return;

    // calculate the mid point
    int mid = l + ((r - l) / 2);

    // divide the array into two halves
    // call to sort the first half
    mergeSort(arr, l, mid);

    // call to sort the second half
    mergeSort(arr, mid + 1, r);

    // once the individual halves are sorted, merge both halves
    merge(arr, l, mid, r);
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