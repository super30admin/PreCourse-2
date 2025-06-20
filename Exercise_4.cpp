// Time Complexity :O(nlogn)
// Space Complexity :O(n) - for copying l[],r[]
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach


#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    // create two sub arrays 
    // has 3 indices left right and main 
    //for keeping track of the indices of the three arrays
    int n1 = (m-l) +1;
    int n2 = r - m;
    int left_arr[n1], right_arr[n2];

    for(int i = 0; i <= n1; i++){  //left array 
        left_arr[i] = arr[i];
    }
    for(int j = 0; j <= n2; j++){   // right array
        right_arr[j] = arr[j + m + 1];
    }
    //creating indices
    int left = 0;
    int right = 0;
    int main = l; //given l index

    while(left < n1 && right < n2){
        if(left_arr[left] <= right_arr[right]){
            arr[main] = left_arr[left];
            main++;
            left++;
        }
        else{
            arr[main] = right_arr[right];
            main++;
            right++;
        }
    }

    while(left < n1){ //no comparision is there
        arr[main] = left_arr[left];
        main++;
        left++;
    }
    while(right < n2){
        arr[main] = right_arr[right];
        main++;
        right++;
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
   if(l < r){
    int m = l + ((r-l)/2);
    mergeSort(arr, l, m); // First subarray is arr[l..m] 
    mergeSort(arr, m+1, r);// Second subarray is arr[m+1..r] 

    merge(arr, l,m,r);// Merges two subarrays of arr[]. 
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