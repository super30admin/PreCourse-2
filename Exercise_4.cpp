/**
 * Time complexity:
 * O(nlogn)
 */

/**
 * Space Complexity:
 * O(n)
 * 
 */

/**
 * Approach:
 * Merge sort follows the technique of dividing the array into two halves
 * Then comparing them and merging them back. 
 */

// The code ran perfectly


#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int lLength = m - l + 1;
    int rLength = r - m;

    int *lSubarray = new int(lLength);
    int *rSubarray = new int(rLength);

    for(int i =0; i<lLength; i++){
        lSubarray[i] = arr[l + i];
    }
    for(int j =0; j<rLength; j++){
        rSubarray[j] = arr[m + 1 + j];
    }

    auto idxArrOne = 0;
    auto idxArrTwo = 0;
    int idxArrMer = l;

    while(idxArrOne < lLength && idxArrTwo < rLength){
        if(lSubarray[idxArrOne] <= rSubarray[idxArrTwo]){
            arr[idxArrMer] = lSubarray[idxArrOne];
            idxArrOne++;
        } else {
            arr[idxArrMer] = rSubarray[idxArrTwo];
            idxArrTwo++;
        }
        idxArrMer++;
    }

    while(idxArrOne < lLength){
        arr[idxArrMer] = lSubarray[idxArrOne];
        idxArrOne++;
        idxArrMer++;
    }

    while(idxArrTwo < rLength){
        arr[idxArrMer] = rSubarray[idxArrTwo];
        idxArrTwo++;
        idxArrMer++;
    }

} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here

    if(l >= r) return;

    auto mid  = l + (r - l)/2;
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