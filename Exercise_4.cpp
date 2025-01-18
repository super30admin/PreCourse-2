// Time complexity is O(nlogn)
// Space complexity is O(n)
// Code ran successfully with the following output

// Given array is 
// 12 11 13 5 6 7 

// Sorted array is 
// 5 6 7 11 12 13 


// === Code Execution Successful ===

#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int s1 = m - l + 1;
    int s2 = r - m;
    int left[s1], right[s2]; // creating Two subarrays temporarily holding elements and populating
    for(int i = 0; i < s1; i++){
        left[i] = arr[l + i];
    }
    for(int j = 0; j < s2; j++){
        right[j] = arr[m + 1 + j];
    }

    int i = 0, j = 0, k = l; //Maintaing the indices

    while(i < s1 && j < s2){ //Picking larger element until reaching end of one of two arrays
        if(left[i] <= right[j]){
            arr[k] = left[i];
            i++;
        }
        else{
            arr[k] = right[j];
            j++;
        }
        k++;
    }
    //Once we have exhausted one of the arrays, copying from the other
    while(i < s1){
        arr[k] = left[i];
        i++;
        k++;
    }

    while(j < s2){
        arr[k] = right[j];
        j++;
        k++;
    }

} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if(l < r){
        int mid = l + (r - l)/2;
        mergeSort(arr, l, mid);
        mergeSort(arr, mid + 1, r);
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
    return 0; 
}