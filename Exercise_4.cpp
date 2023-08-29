#include<stdlib.h> 
#include<stdio.h> 
  //Time complexity of Merge sort: O(nlogn)
  //space complexity: O(n)
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    int n1= m-l+1;
    int n2= r-m;
    int L[n1], M[n2];

    for(int i=0;i<n1;i++)
    {
        L[i]=arr[l+i];
    }
    for(int j=0;j<n2;j++)
    {
        M[j]=arr[m+1+j];
    }
    int i=0, j=0, k=l;
    while(i<n1 and j<n2)
    {
        if(L[i]<=M[j])
        {
            arr[k]=L[i];
            i++;
        }
        else
        {
            arr[k]=M[j];
            j++;
        }
        k++;
    }
    while(i<n1)
    {
        arr[k]=L[i]; i++;
        k++;
    }
    while(j<n2)
    {
        arr[k]=M[j]; j++;
        k++;
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
   if(l>r)
    return;
    int mid=(l+r)/2;
    mergeSort(arr, l, mid);
    mergeSort(arr, mid+1, r);
    merge(arr, l , mid, r);
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