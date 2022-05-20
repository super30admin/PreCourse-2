
// Time Complexity : Average case O( n log(n) ) as each time the array gets divided into two parts ( log n ) and iteration of those two subarray causes multiplication by n.
                     // worst case also O( n log(n) ). 
// Space Complexity : O(n) , a new array taken which is sorted finally and copied over. Not in place.
// Any problem you faced while coding this : None

// Your code here along with comments explaining your approach
/* Divide and conquer approach on array and bottom up keep sorting each two halves of subarray. */

#include<iostream>
using namespace std;
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int left = l;
    int leftend = m;
    int right = m+1;
    int rightend = r;
    int i = l;
    int temp[r];
    while( left <= leftend && right <=rightend ){
       if( arr[left] < arr[right] ){
          temp[i] = arr[left];
          left++;
       } else {
          temp[i] = arr[right];
          right++;
       }
       i++;
    }
    // fill left over array, whichever was longer will be left
    // only one while exectues from below
    while( left <= leftend ){
        temp[i] = arr[left];
        left++;
        i++;
    }
    while( right <= rightend ){
        temp[i] = arr[right];
        right++;
        i++;
    }
    // copy over the final array
    for( int i=l; i<=r; i++) {
        arr[i] = temp[i];
    } 
}
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if( l >= r ){  // first execution of merge should have one element arrays
       return;
    }
    int mid = (l + r)/2;
    mergeSort( arr, l, mid );
    mergeSort( arr, mid+1, r );
    merge( arr, l, mid, r );
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
