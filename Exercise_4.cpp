// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach


#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int finalIndex;
    int n1 = m - l + 1;
    int n2 = r - m;
    int arr1[n1], arr2[n2];
    for(int i = 0; i < n1; i++)
        arr1[i] = arr[l + i];
    for(int j = 0; j < n2; j++)
        arr2[j] = arr[m + 1 + j];
    int index1 = 0, index2 = 0;
    finalIndex = l;
    while(index1 < n1 && index2 < n2) {
        if (arr1[index1] < arr2[index2]) {
            arr[finalIndex] = arr1[index1];
            index1++;
        }
        else {
            arr[finalIndex] = arr2[index2];
            index2++;
        }
        finalIndex++;
    }

    while(index1 < n1) {
        arr[finalIndex] = arr1[index1];
        index1++;
        finalIndex++;
    }
    while (index2 < n2) {
        arr[finalIndex] = arr2[index2];
        index2++;
        finalIndex++;
    }
    
}
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m); // Before m
        mergeSort(arr, m + 1, r); // After m
        merge(arr, l, m, r);
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