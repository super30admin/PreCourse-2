// Time Complexity : O(nlogn)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode :yes
// Any problem you faced while coding this : no

#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    vector<int>res;
    int i=l;
    int j=m+1;
    while((i <= m) && (j <= r)) {
        if(arr[i] <= arr[j]) {
            res.push_back(arr[i]);
            i++;
        } else {
            res.push_back(arr[j]);
            j++;
        }
    }
    while(i<=m){
        res.push_back(arr[i]);
        i++;
    }
    while(j<r){
        res.push_back(arr[j]);
        j++;
    }
    for(int i=0; i<res.size();i++){
        arr[l] = res[i];
        l++;
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    int mid =0;  
    if(l<r){
    mid = l+(r-l)/2;
    mergeSort(arr, l, mid);
    mergeSort(arr, mid+1, r);
    merge(arr, l, mid, r);  
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
    
    int arr1[] = { 1, 2, 3, 2, 1, -9, 8, 4, 2, 7}; 
    int arr1_size = sizeof(arr1)/sizeof(arr1[0]); 
  
    printf("Given array is \n"); 
    printArray(arr1, arr1_size); 
  
    mergeSort(arr1, 0, arr1_size - 1); 
  
    printf("\nSorted array is \n"); 
    printArray(arr1, arr1_size); 
    return 0; 
}
