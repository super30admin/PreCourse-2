/*
Time Complexity: O(nlog(n)) - Because array division into halves takes log(n) and then merge takes n.
Space Complexity: O(n) - during merge it takes O(n)
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No
*/

#include<stdlib.h> 
#include<stdio.h> 
#include <vector>
#include <iostream>

using namespace std;
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    vector<int> temp;
    int l1 = l;
    int l2 = m+1;
    while (l1 <= m && l2 <= r) {
        if (arr[l1] <= arr[l2]) {
            temp.push_back(arr[l1]);
            l1++;
        }
        else {
            temp.push_back(arr[l2]);
            l2++;
        }
    }
    while (l1<= m) {
        temp.push_back(arr[l1]);
        l1++;
    }
    while (l2<= r) {
        temp.push_back(arr[l2]);
        l2++;
    }

    for (int i = l; i<=r; i++){
        arr[i] = temp[i-l];
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    int mid = (r+l)/2;
    if (l>=r) return;
    mergeSort(arr, l, mid);
    mergeSort(arr, mid+1, r);
    
    merge(arr, l, mid, r);
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