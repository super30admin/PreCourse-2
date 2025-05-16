#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    int p1=m-l+1,p2=r-m;
    int temp1[p1],temp2[p2];
    for(int i=0;i<p1;i++){
        temp1[i] = arr[l+i];
    }
    for(int j=0;j<p2;j++){
        temp2[j] = arr[m+j+1];
    }
    int i=0,j=0,k=l;
    while(i<p1 && j<p2){
        if(temp1[i] <= temp2[j]){
            arr[k++] = temp1[i++];
        }else{
            arr[k++] = temp2[j++];
        }
    }
    while(i<p1){
        arr[k++] = temp1[i++];
    }
    while(j<p2){
        arr[k++] = temp2[j++];
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    if(l<r)
    {
        int mid = l+(r-l)/2;
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