/*
 *                     Merge Sort Alorithm
 *
 * Time Complexity  :  O(nlogn)
 * Space Complexity :  O(n) 
 * Did this code successfully run on Leetcode/VSCode : Yes
 * Any problem you faced while coding this : No 
 * Your code here along with comments explaining your approach :
 *          Using divide and conquer technique.
 */
#include<iostream>
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int nL = m - l + 1;
    int nR = r - m;

    int L[nL], R[nR];

    for(int i = 0; i < nL; i++) {
        L[i] = arr[l+i];
    }
    for(int i = 0; i < nR; i++) {
        R[i] = arr[m + 1 + i];
    }

    int i = 0, j = 0;
    int k = l;

    while (i < nL && j < nR) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < nL) {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < nR) {
        arr[k] = R[j];
        j++;
        k++;
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if (l < r) {
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