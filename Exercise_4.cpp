#include<stdlib.h> 
#include<stdio.h> 
#include <iostream>

using namespace std;
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{
    int i, j, k;
    int ln = m - l + 1, rn = r - m; 
    int left[ln], right[rn];

    for (i = 0; i < ln; i++) {
        left[i] = arr[l + i];
    }

    for (j = 0; j < rn; j++) {
        right[j] = arr[m + j + 1];
    }

    for (i = 0, j = 0, k = l; (i < ln) && (j < rn); k++) {
        if (left[i] <= right[j]) {
            arr[k] = left[i++];
        } else {
            arr[k] = right[j++];
        }
    }

    for (; i < ln; i++, k++) {
        arr[k] = left[i];
    }

    for (; j < rn; j++, k++) {
        arr[k] = right[j];
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    if (l >= r) {
        return;
    }

    int m = (l + ((r - l) / 2));
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);
    merge(arr, l, m, r);
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
