#include<stdlib.h> 
#include<stdio.h> 
#include<bits/stdc++.h>
#include<vector>
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
//tc-O(NLogN)
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int start=0;
    int right=m+1;
vector<int>temp;
while(start<m&&right<r){
    if(arr[start]<arr[right]){
        temp.push_back(arr[start++]);
    }
    else{
        temp.push_back(arr[right++]);
    }
}
while(start<m){
    temp.push_back(arr[start++]);

}
while(right<r){
    temp.push_back(arr[right++];)
}
for(int i=0;i<(r-l+1);i++){
    arr[i]=temp[i-start];
}

} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if(l>=r)return ;

    int mid=(l+r)>>1;
    mergesort(arr,l,mid);
    mergesort(arr,mid+1,r);
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