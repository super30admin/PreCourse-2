/* Time Complexity = O(n * log(n))
   Space Complexity = O(n) */
#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{   
    //We create a temporary array to store the merged array, with tempPos as position indicator, and n as the size of array
    int n = r - l + 1;
    int tempArr[n];
    int tempPos = l;
    int leftEnd = m - 1;

    while (l <= leftEnd && m <= r) 
    {
        if (arr[l] <= arr[m])
            tempArr[tempPos++] = arr[l++];
        else
            tempArr[tempPos++] = arr[m++];
    }

    //Copying rest of left half
    while (l <= leftEnd)
        tempArr[tempPos++] = arr[l++];

    //Copying rest of right half
    while (m <= r)
        tempArr[tempPos++] = arr[m++];

    /*Copying temporary array back to the original from back to front,
        because only the rightmost position is an accurate indicator for the edge of the array*/
    for (int i = 0; i < n; i++, r--)
    {
        arr[r] = tempArr[r];
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{   
    //We do not do left<=right, because we need atleast two elements in the array to divide and merge later
    if (l < r) 
    {
        int m = (l + r) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m + 1, r);    
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