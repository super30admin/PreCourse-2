// Time Complexity - For the merge() function time complexity is O(n)
// Time complexity for mergeSort algorithm implemented below(recursively) is O(nlogn) for best, worst and normal scenarios.

// Problems Faced - No!

#include<stdlib.h>
#include<stdio.h>
  
// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r)
{
    //Your code here
    int i = l, k = l;
    int j = m+1;
    int tempArr[r+1];
    
    while(i <= m && j <= r){
        if(arr[i] > arr[j])
            tempArr[k++] = arr[j++];
        else
            tempArr[k++] = arr[i++];
    }
    
    // copy elements from first subarray if second subarray is empty after the above while loop
    for(;i <= m; i++)
        tempArr[k++] = arr[i];
    
    // copy elements from second subarray if first subarray is empty after the above while loop
    for(;j <= r; j++)
        tempArr[k++] = arr[j];
    
    // copy elements from tempArr to our original array
    for(i = l; i <= r; i++)
        arr[i] = tempArr[i];
}
  
/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
    //Your code here
    if(l < r){
        int mid = l + (r-l)/2;
        mergeSort(arr, l, mid);
        mergeSort(arr, mid+1, r);
        merge(arr, l, mid, r);
    }
}
  
/* UTILITY FUNCTIONS */
/* Function to print an array */
void printArray(int A[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}
  
/* Driver program to test above functions */
int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr)/sizeof(arr[0]);
  
    printf("Given array is \n");
    printArray(arr, arr_size);
  
    mergeSort(arr, 0, arr_size - 1);
  
    printf("\nSorted array is \n");
    printArray(arr, arr_size);
    return 0;
}
