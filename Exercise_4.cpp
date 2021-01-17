#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int i,j,k,x=m-l+1,y=r-m;
    int L[x], R[y];
 
    for (i=0;i<x;i++)
        L[i]=arr[l+i];
    for (j=0;j<y;j++)
        R[j]=arr[m+1+j];
 
    
    i=0,j=0,k=l; 
     
    while (i<x && j<y) 
    {
        if (L[i] <= R[j]) 
        {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 
    
    while (i<x) 
    {
        arr[k] = L[i];
        i++;
        k++;
    }
 
   
    while (j<y) 
    {
        arr[k] = R[j];
        j++;
        k++;
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if (l<r) 
    {    
        int x = (l+r)/2;
        mergeSort(arr,l,x);
        mergeSort(arr,x+1,r);
 
        merge(arr,l,x,r);
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
