#include<stdlib.h> 
#include<stdio.h>
#include <bits/stdc++.h>
using namespace std;
/*
Time complexity - O(NlogN)
Space complexity - O(N) //recursion stack
*/

// A utility function to swap two elements  
void swap(int* a, int* b)  
{  
    //Your Code here 
    int c = (*a);
    (*a) = (*b);
    (*b) = c;
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

  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int l1 = m - l + 1; //length of left arr
    int l2 = r - m; // length of right arr
    int arr1[l1], arr2[l2];
    // copy left and right arrays
    for (int i = 0; i < l1; ++i){
        arr1[i] = arr[l + i];
    }
    for (int i = 0; i < l2; ++i){
        arr2[i] = arr[m + i + 1];
    }
    // merge the two arrays
    int i = 0, j = 0, k = l;
    while (i < l1 && j < l2){
        if (arr1[i] < arr2[j]) arr[k++] = arr1[i++];
        else arr[k++] = arr2[j++];
    }
    //copy the rest of the array
    while(i < l1) arr[k++] = arr1[i++];
    while(i < l2) arr[k++] = arr2[j++];
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if (l < r){
        int mid = l + (r - l) / 2;
        mergeSort(arr, l, mid);
        mergeSort(arr, mid + 1, r);
        merge(arr, l, mid, r);
    }
} 
  

  
/* Driver program to test above functions */
int main() 
{ 
    int arr[] = {12, 11, 13, 5, 6}; 
    int arr_size = sizeof(arr)/sizeof(arr[0]); 
  
    printf("Given array is \n"); 
    printArray(arr, arr_size); 
  
    mergeSort(arr, 0, arr_size - 1); 
  
    printf("\nSorted array is \n"); 
    printArray(arr, arr_size); 
    return 0; 
}
