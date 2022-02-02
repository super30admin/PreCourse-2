#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r]

// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : No

void merge(int arr[], int l, int m, int r) 
{ 
    int len1 = m - l + 1;
    int len2 = r - m;

    // Create temp arrays
    int leftarr[] = new int[len1];
    int rightarr[] = new int[len2];

    // Copying values into temp arrays
    for(int i = l; i < m - 1; i++)
        leftarr[i] = arr[i];
    
    for(int i = m; i < r; i++)
        rightarr[i - m] = arr[i];
    
    int mergedindex = l;
    int i = 0, j = 0;

    while(i < len1 && j < len2) {
        if(leftarr[i] < rightarr[j]) {
            arr[mergedindex] = leftarr[i];
            i++;
        } 
        else {
            arr[mergedindex] = rightarr[j];
            j++
        }
        mergedindex++;
    }

    while(i < len1) {
        arr[mergedindex] = leftarr[i];
        i++;
        mergedindex++;
    }

    while(j < len2) {
        arr[mergedindex] = rightarr[j];
        j++;
        mergedindex++;
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    if(r > l) {
        // Middle of the arr[]
        int m = (l + r - 1)/2;
        // Left half
        mergeSort(arr, l, m-1);
        // Right half
        mergeSort(arr, m+1, r);
        // Merge both the halves
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