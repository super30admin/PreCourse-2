#include<stdlib.h> 
#include<stdio.h> 

//TC: O(nlog n)
//SC: O(n) where n is number of elements
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
  
  int l_len = m - l + 1;
  int r_len = r- m;

  int left_arr[l_len];
  int rig_arr[r_len];

  int i=0, j=0;
  for(i=0; i<l_len; i++)
    left_arr[i] = arr[l+i];
  
  for(j = 0; j<r_len; j++)
    rig_arr[j] = arr[m + 1 + j];
  

  //merging two arrays
  i = 0; 
  j = 0; 
  int k = l; //starting point in original array

  while(i < l_len && j < r_len){
    if(left_arr[i] <= rig_arr[j]){ 
      arr[k] = left_arr[i];
      i++;
    } else{
      arr[k] = rig_arr[j];
      j++;
    }
    
    k++;
  }


  //put remaining elements from whichever array has them

  while(i < l_len){
    arr[k] = left_arr[i];
    i++; k++;
  }

  while(j < r_len){
    arr[k] = rig_arr[j];
    j++; k++;
  }



    //Your code here
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
  if(l >= r)
    return;
  
  int mid = l + (r - l)/2;
  mergeSort(arr, l, mid);
  mergeSort(arr, mid+1, r);
  merge(arr, l, mid, r);
    //Your code here
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