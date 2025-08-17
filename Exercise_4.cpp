/*
TC: Since we are halving the array at each step, the max number of halvings till we hit a subarray of size 1 (only one element) is log n. 
The work done at each level in the recursion tree = n, since we are going over each subarray and merging.
                                [4, 2, 1, 3]
                                /          \
                             [4, 2]      [1, 3] => n elements in total need to be merged 
                             /    \      /    \
                           [4]    [2]  [1]    [3]                       
Therefore, since there are log n levels and each level requires n work, the total TC is O(nlogn).
SC: At each level in the recursion tree, we need to create temp arrays for merging. The total space needed at each level is O(n). The recursion 
stack also takes up space, since we have a recursion tree of depth log n, the recursion space will be O(logn).
Therefore total space = O(n + logn) which is asymptotically O(n).

Explanation in Sample.java
*/

#include <bits/stdc++.h>

using namespace std;
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int i = l; // left subarray iterator
    int j = m+1; // right subarray iterator
    int k = 0; // merged array iterator
    int len = r - l + 1; // length of merged subarray
    int merged[len];

    while(i <= m && j <= r){ // merge elements in sorted order from left & right subarrays into merged
        if(arr[i] <= arr[j]) {
            merged[k] = arr[i];
            i++;
        } else {
            merged[k] = arr[j];
            j++;
        }
        k++;
    }

    while(i <= m) { // merge leftover elements from left subarray (if any)
        merged[k] = arr[i];
        i++;
        k++;
    }
    while(j <= r) { // merge leftover elements from right subarray (if any)
        merged[k] = arr[j];
        j++;
        k++;
    }
    int x = l;
    k = 0;
    while(x<=r && k < len){ // change the original array to now have sorted elements from index l to r
        arr[x] = merged[k];
        k++;
        x++;
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if(l < r){
        int mid = l + (r-l)/2;
        mergeSort(arr, l, mid); // call mergeSort on left half
        mergeSort(arr, mid+1, r); // call mergeSort on right half
        merge(arr, l, mid, r); // merge the left and right halves
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

bool isSorted(int A[], int size) {
    for(int i=1; i<size; i++){
        if(A[i-1] > A[i]) return false;
    }
    return true;
}
  
/* Driver program to test above functions */
int main() 
{ 
    /* TEST CASES */
    int arr[] = {12, 11, 13, 5, 6, 7}; // normal array
    // int arr[] = {}; // empty array
    // int arr[] = {1}; // array with only one element (already sorted)
    // int arr[] = {1, 2, 3, 4}; // already sorted array
    // int arr[] = {1, 3, 2, 1, 2, 3, 4, 1, 4, 2, 3}; // array with duplicates
    // int arr[] = {5,-1,3,0,-2,4,-3}; // negatives
    // int arr[] = {INT_MIN, 0, INT_MIN, INT_MAX}; // extreme values

    int arr_size = sizeof(arr)/sizeof(arr[0]); 
    if(arr_size == 0) {
        cerr<<"Invalid array"<<endl;
        return 1;
    } 
    
    printf("Given array is \n"); 
    printArray(arr, arr_size);

    if(arr_size == 1 || isSorted(arr, arr_size)){
        cout<<"Array is already sorted."<<endl;
        return 0;
    } 
  
    mergeSort(arr, 0, arr_size - 1); 
  
    printf("\nSorted array is \n"); 
    printArray(arr, arr_size); 
    return 0; 
}