// Time Complexity : O(NlogN)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode : NA
// Any problem you faced while coding this : None

#include<iostream>

using namespace std;
 
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 

    int* temp_array = (int*) malloc(sizeof(int) * (r - l + 1));

    int i = l, j = m + 1, k = 0;

    while (i <= m && j <= r) 
    {
        if (arr[i] <= arr[j]) 
        {
            temp_array[k] = arr[i];
            k += 1; i += 1;
        }
        else 
        {
            temp_array[k] = arr[j];
            k += 1; j += 1;
        }
    }


    while (i <= m) 
    {
        temp_array[k] = arr[i];
        k += 1; i += 1;
    }


    while (j <= r) 
    {
        temp_array[k] = arr[j];
        k += 1; j += 1;
    }


    for (i = l; i <= r; i += 1) 
    {
        arr[i] = temp_array[i - l];
    }


} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if (l < r)
    {
        int mid = l + (r - l) / 2;
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