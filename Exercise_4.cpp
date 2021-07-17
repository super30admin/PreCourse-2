#include<stdlib.h> 
#include<stdio.h> 
#include<vector>
using namespace std;
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int left_size = m - l + 1;
    int right_size = r - m;

    vector<int> left_arr(left_size);
    vector<int> right_arr(right_size);

    for(int i = 0; i < left_size; i++)
        left_arr[i] = arr[l + i];
    
    for(int i = 0; i < right_size; i++)
        right_arr[i] = arr[m+1+i];
    
    int left = 0, right = 0, arr_index = l;
    
    while(left < left_size && right < right_size){
        if(left_arr[left] < right_arr[right]){
            arr[arr_index] = left_arr[left];
            left++;
        }
        else{
            arr[arr_index] = right_arr[right];
            right++;
        }
        arr_index++;
    }

    while(left < left_size){
        arr[arr_index] = left_arr[left];
        left++;
        arr_index++;
    }
    
    while(right < right_size){
        arr[arr_index] = right_arr[right];
        right++;
        arr_index++;
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{
    //Your code here 
    if(l >= r)
        return;

    int mid = (l + r)/2;
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
    int arr[] = {12, 11, 13, 5, 6, 7, 8, 10}; 
    int arr_size = sizeof(arr)/sizeof(arr[0]); 
  
    printf("Given array is \n"); 
    printArray(arr, arr_size); 
  
    mergeSort(arr, 0, arr_size - 1); 
  
    printf("\nSorted array is \n"); 
    printArray(arr, arr_size); 
    return 0; 
}