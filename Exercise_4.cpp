#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int b[r-l+2];
    int il=l,ir=m+1,ib=0;
    while(il<=m && ir<=r){
        if(arr[il]<arr[ir]){
            b[ib]=arr[il];il++;
        }
        else if(arr[il]>arr[ir]){
            b[ib]=arr[ir];ir++;
        }
        else{
            b[ib]=arr[ir];
            ir++;ib++;
            b[ib]=arr[il];
            il++;
        }
        ib++;
    }
    while(il<=m){
        b[ib]=arr[il];il++;ib++;
    }
    while(ir<=r){
        b[ib]=arr[ir];ir++;ib++;
    }
    int itr=l,io=0;
    while(itr<=r){
        arr[itr]=b[io];io++;itr++;
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    int mid=(l+r)/2;
    if(l>=r){
        return;
    }
    mergeSort(arr,l,mid);
    mergeSort(arr,mid+1,r);
    merge(arr,l,mid,r);
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