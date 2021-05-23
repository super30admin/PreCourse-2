//Time Complexity: O(n log n)
//Space Complexity: O(n) since we create new arrays 
#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    int i, j, k;
    int s1 = m - l + 1;
    int s2 = r - m;
    int arrL[s1];
    int arrR[s2];

    for(i = 0; i < s1; i++){
        arrL[i] = arr[l + i];
    }
    for(j = 0; j < s2; j++){
        arrR[j] = arr[m + 1 + j];
    }

    i = 0;
    j = 0;
    k = l;

    while( i < s1 && j < s2){
        if(arrL[i] <= arrR[j]){
            arr[k] = arrL[i];
            i++;
        }
        else {
            arr[k] = arrR[j];
            j++;
        }
        k++;
    }

    while(i < s1){
        arr[k] = arrL[i];
        i++;
        k++;
    }
    
    while(j < s2){
        arr[k] = arrR[j];
        j++;
        k++;
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    if(l < r){
    int mid = l+(r-l)/2;
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