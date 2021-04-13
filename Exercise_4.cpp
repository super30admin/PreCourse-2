#include<stdlib.h> 
#include<stdio.h>  
#include<bits/stdc++.h>
using namespace std;
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
// Time - O(nlogn) n being the size of the array
// Space - O(n) Temp arrays

void merge(int arr[], int l, int m, int r) 
{ 
    
    //Your code here
    int sz1 = m-l+1;
    int sz2 = r-m;
    int temp1[sz1];
    int temp2[sz2];
    for(int i=0;i<sz1;i++){
        temp1[i] = arr[l+i];
    }
    for(int j=0;j<sz2;j++){
        temp2[j] = arr[m+1+j];
    }
    int k=l,i=0,j=0;
    while(i<sz1 && j<sz2){
        if(temp1[i]<=temp2[j]){
            arr[k++] = temp1[i];
            i++;
        }
        else{
            arr[k++] = temp2[j];
            j++;
        }
    }
    while(i<sz1){
        arr[k++] = temp1[i];
        i++;
    }
    while(j<sz2){
        arr[k++] = temp2[j];
        j++;
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if(l>=r)
        return;
    int mid = l + (r-l)/2;
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