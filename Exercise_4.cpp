// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Any problem you faced while coding this : Issues with merge technique
#include<iostream>  
#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    //To store starting position of both subarrays
    int leftPos = l;
    int rightPos = m+1;
    int newarrPos = 0;

    int newarr[r-l+1];
    for(int i = l; i<= r; i++)
    {
        if(leftPos > m)
        {
            newarr[newarrPos] = arr[rightPos];
            newarrPos++; 
            rightPos++;
        }
        else if(rightPos > r)
        {
            newarr[newarrPos] = arr[leftPos];
            newarrPos++;
            leftPos++;
        }
        else if(arr[leftPos] < arr[rightPos])
        {
            newarr[newarrPos] = arr[leftPos];
            newarrPos++;
            leftPos++;
        }
        else
        {
            newarr[newarrPos] = arr[rightPos];
            newarrPos++;
            rightPos++;
        }
    }

    for(int leftPos = 0; leftPos < newarrPos; leftPos++)
    {
        arr[l] = newarr[leftPos];
        l++;
    }
    return;
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if(l<r)
    {
        //divide the array into 2 subarrays
        int mid = (l + ((r-l)/2));
        mergeSort(arr, l, mid-1);
        mergeSort(arr, mid+1, r);
        // Merge the sorted subarrays
        merge(arr, l, mid, r);
    }
    return;
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