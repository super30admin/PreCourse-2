#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int num_1 = m-l+1;
    int num_2 = r-m;
    //the above 2 should add to r-l+1; 
    int Left_array[num_1];
    int Right_array[num_2];
    
    
    // Copy data to temp arrays L[] and R[]
    for (int i = 0; i < num_1; i++)
        Left_array[i] = arr[l + i];
    for (int j = 0; j < num_2; j++)
        Right_array[j] = arr[m + 1 + j];
    
        int i = 0;
 
    int j = 0;
    int k = l;
 
    while (i < num_1 && j < num_2) {
        if (Left_array[i] <= Right_array[j]) {
            arr[k] = Left_array[i++];
        }
        else {
            arr[k] = Right_array[j];
            j++;
        }
        k++;
    }
 
    while (i < num_1) {
        arr[k++] = Left_array[i++];
    }
    
    while (j < num_2) {
        arr[k++] = Right_array[j++];
    }
    
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if(l>=r){
        return;
    }
    
    int mid = l+(r-l)/2;
    //I did not want to change existing code, else Id put low/hi for better understading
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
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
