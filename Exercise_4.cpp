#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int n_final = r-l+1;
    int temp[n_final];
    int p1 = l, p2 = m+1,temp_p = 0;
    while(p1<=m&&p2<=r){
        if(arr[p1]<=arr[p2]){
            temp[temp_p] = arr[p1];
            p1++;
        }
        else{
            temp[temp_p] = arr[p2];
            p2++;
        }
        temp_p++;
    }
    while(p1<=m){
        temp[temp_p] = arr[p1];
        p1++;
        temp_p++;
    }
    while(p2<=r){
        temp[temp_p] = arr[p2];
        p2++;
        temp_p++;
    }
    for(int i=0;i<n_final;i++){
        arr[l+i] = temp[i];
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if(l>=r) return;
    int mid = l+(r-l)/2;
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