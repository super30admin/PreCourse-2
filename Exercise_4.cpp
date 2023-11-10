#include<bits/stdc++.h> 

// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    int size = r + 1 - l;
    int tempArr[size];

    int f, s, i;
    f = l;
    s = m + 1;
    i = 0;

    //Your code here
    while (f <= m && s <= r)
    {
        if (arr[f] < arr[s])
        {
            tempArr[i++] = arr[f++];
        }
        else
        {
            tempArr[i++] = arr[s++];
        }
    }

    while (f <= m)
    {
            tempArr[i++] = arr[f++];
    }

    while (s <= r)
    {
            tempArr[i++] = arr[s++];
    }

    for (i = 0; i < size; i++)
    {
        arr[l+i] = tempArr[i];
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */

// Time Complexity : O(n log n)
// Space Complexity : O(n)

/* Recursively divide the array into two parts until the two arrays of single values are formed.
*  Then start merging the arrays in sorted manner as recursion stack unwinds. 
*/
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if (l == r) 
        return;
    int mid = l + ((r - l) / 2);

    mergeSort(arr, l, mid);
    mergeSort(arr, mid + 1, r);
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