#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    int n1=m-l+1; // for size of temporary arrays
    int n2=r-m; // for sizes of temporary arrays


    int L[n1], R[n2];

    for(int i=0;i<n1;i++)
    L[i]=arr[l+i];
    for(int i=0;i<n2;i++)
    R[i]=arr[m+1+i];

    int i=0; // index of first array
    int j=0; // index of second array
    int k=l; // index of new merged array

    while(i<n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k]=L[i];
            i++;
        }
        else
        {
            arr[k]=R[j];
            j++;
        }
        k++;
        
    }

    //now if there are unequal number of elements
    while (i < n1) 
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j<n2)
    {
        arr[k]=R[j];
        j++;
        k++;
    }
    




} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    if(l>=r)
    return;

    int m=(l+r-1)/2;



    mergeSort(arr,l,m);
    mergeSort(arr,m+1,r);
    merge(arr,l,m,r);

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