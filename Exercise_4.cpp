// Time Complexity : O(N log N)
// Space Complexity: O(N)
// Did this code successfully run on Leetcode : Not available on leetcode
// Any problem you faced while coding this : None


#include<stdlib.h>
#include<stdio.h>
  
// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r)
{
    //Your code here
    int size1 = m-l+1;
    int size2 = r-m;
    
    // creating two temporary arrays
    int left[size1], right[size2];
    
    
    for(int i = 0; i < size1; i++){
        left[i] = arr[l+i];
    }
    for(int i = 0; i < size2; i++){
        right[i] = arr[m+1+i];
    }
    
    int i = 0, j = 0, k = l;
    
    while(i < size1 && j < size2){
        if(left[i] <= right[j]){
            arr[k] = left[i];
            i++;
        }
        else{
            arr[k] = right[j];
            j++;
        }
        k++;
    }
    
    while(i < size1){
        arr[k] = left[i];
        i++;
        k++;
    }
    
    while(j < size2){
        arr[k] = right[j];
        j++;
        k++;
    }
}
  
/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
    //Your code here
    if(l < r){
        int mid = (l+r)/2;
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
