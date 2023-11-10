// Time Complexity : O(nlogn) where n is number of elements  
// Space Complexity : O(n)  where n is number of elements 
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int count1 = m - l + 1;
    int count2 = r - m;

    int array1[count1], array2[count2];
    for(int i=0;i<count1;i++)
    {
        array1[i] = arr[l+i];
    }
    for(int j=0; j<count2;j++)
    {
        array2[j] = arr[m+j+1];
    }

    int i=0;
    int j=0;
    int k = l;
    while(i< count1 && j<count2)
    {
        if(array1[i] < array2[j])
        {
            arr[k] = array1[i];
            k++;
            i++;
        }
        else
        {
            arr[k] = array2[j];
            k++;
            j++;
        }
        
    }

    while (i < count1) {
        arr[k] = array1[i];
        i++;
        k++;
    }
 
    while (j < count2) {
        arr[k] = array2[j];
        j++;
        k++;
    }

} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if(l<r)
    {
        int mid = (l + r)/2;
        mergeSort(arr,l,mid);
        mergeSort(arr,mid+1,r);
        merge(arr,l,mid,r);
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