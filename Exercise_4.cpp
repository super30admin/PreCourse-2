// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Any problem you faced while coding this : Yes! Even the slightlest mistake in indexing of the arrays can lead to headaches and frustation!


// Your code here along with comments explaining your approach

#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int n1 = m-l + 1; // size of subarray1
    int n2 = r-m;  // size of subarray2
    int arr1[n1], arr2[n2]; // creating 2 subarrays
    for (int i = 0; i < n1; i++)
    {
        arr1[i] = arr[i+l]; // inserting elements in left subarray
    }
    for (int j = 0; j < n2; j++)
    {
        arr2[j] = arr[m+1+j]; // inserting elements in left subarray
    }

    int i =0, j = 0, k = l;  // index of both subarrays and main array
    while (i<n1 && j< n2) // comparing elements in both subrrays, the least element is put into main array
    {
        if(arr1[i] <= arr2[j]) 
        {
            arr[k] = arr1[i];
            i++;
        }
        else{
            arr[k] = arr2[j];
            j++;
        }
        k++;
    } 
    while(i<n1) // if elements are remaining in the left subarray, they are inserted into main array
    {
        arr[k] = arr1[i];
        i++;
        k++;
    }  
    while(j<n2) // if elements are remaining in the right subarray, they are inserted into main array
    {
        arr[k] == arr2[j];
        j++;
        k++;
    }
          
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    
    if(r>l){        // base condition
        int mid = l + (r-l)/2;
        mergeSort(arr, l, mid);       
        mergeSort(arr, mid+1, r);
        merge(arr, l , mid, r);   
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