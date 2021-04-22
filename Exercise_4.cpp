#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    int i =l; int j=m;int k= l;
    int aux_arr[r+1];
    while (i <=m && j<= r)
    {
        if (arr[i]< arr[j]){
                aux_arr[k++] = arr[i++];
        }else{
            aux_arr[k++]= arr[j++];
        }
    }
    for (; i < m; i++)
    {
        aux_arr[k++]= arr[i];
    }
    for (; j < r; i++)
    {
        aux_arr[k++]= arr[j];
    }
    // read this again(reminder for me)
    for (int i = l; i < r; i++)
    {
        arr[i]=aux_arr[i];
    }
    
    
    
    
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    int mid;
    //Your code here
    if(l< r){
        mid= (l+r)/2;
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