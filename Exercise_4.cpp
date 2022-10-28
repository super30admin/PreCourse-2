/*

TC: O(nlgn)
SC: O(n)
Logic: 
1. Divide and conquer algo
Divide the array into parts by splitting in the middle and let recursion sort the left and the right part
2. Then, if we have solutions to the left and right subproblems, can we build the complete solution? Yes! we can merge the two sorted arrays in O(n)

*/


#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    int mergedArr[r-l+1];
    int i=l, j=m+1, k=0;
    while(i <= m && j <= r) {
        if(arr[i] < arr[j]) mergedArr[k] = arr[i], i++;
        else    mergedArr[k] = arr[j], j++;
        k++;
    }
    while(i <= m)   mergedArr[k]=arr[i], i++, k++;
    while(j <= r)   mergedArr[k]=arr[j], j++, k++;
    for(k=0,i=l; k<(r-l+1); k++, i++)
        arr[i] = mergedArr[k];
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    if(l >= r)   return;
    int mid = l+(r-l)/2;
    mergeSort(arr, l, mid);
    mergeSort(arr, mid+1, r);
    merge(arr, l, mid, r);
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