#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here

    int i,j,k; 

    // size_1 is the size of left array.   
    int size_1 = m - l + 1;
    int left_array[size_1];

    // Initializing the left array.
    for(i = 0; i < size_1; i++)
    {
        left_array[i] = arr[l + i];
    }

    // size_2 is the size of right array.
    int size_2 = r - m; 
    int right_array[size_2];

    // Initializing the right array.
    for(j = 0; j < size_2; j++)
    {
        right_array[j] = arr[m + j + 1];
    }

    i = 0;
    j = 0; 

    // Comparing the 2 small arrays and merging them into a new array in sorted order.
    for(k = l; i < size_1 && j < size_2; k++)
    {
        if(left_array[i] < right_array[j])
        {
            arr[k] = left_array[i++];
        }
        else
        {
            arr[k] = right_array[j++];
        }
    }

    // Put remaining elements of left_array[] into arr[].
    while(i < size_1)             
    {
        arr[k++] = left_array[i++];
    }
    
    // Put remaining elements of right_array[] into arr[].
    while(j < size_2)
    {
        arr[k++] = right_array[j++];
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */

// Time Complexity : O(nlogn)
// Space Complexity : O(n)
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
                                   
    if(l < r)
    {
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