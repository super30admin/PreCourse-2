#include<bits/stdc++.h>
using namespace std;
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int i1, int j1, int i2, int j2) 
{ 
    //Your code here
    int i,j,k;
    i = i1;
    j = i2;
    k=0;
    int temp[100];
    while(i<=j1 && j<=j2)
    {
        if(arr[i]<arr[j])
            temp[k++]=arr[i++];
        else
            temp[k++]=arr[j++];
    }
    while(i<=j1)
        temp[k++]=arr[i++];
    while(j<=j2)
        temp[k++]=arr[j++];
    for(i=i1,j=0;i<=j2;i++,j++)
        arr[i] = temp[j];
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    int mid;
    if(l<r)
    {
        mid = l+(r-l)/2;
        mergeSort(arr, l, mid);
        mergeSort(arr, mid+1, r);
        merge(arr,l,mid,mid+1,r);
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
