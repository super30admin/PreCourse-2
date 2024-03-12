// Time Complexity : O(n * log n)           
// Space Complexity : O(1)

#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    int leftArraySize = m-l+1;
    int rightArraySize = r-m;
    //Your code here
    int leftArray[leftArraySize];
    int rightArray[rightArraySize];

    for(int i=0; i<leftArraySize; i++){
        leftArray[i] = arr[l+i];
    }
    for(int i=0; i<rightArraySize; i++){
        rightArray[i] = arr[m+1+i];
    }

    int i=0;
    int j=0;
    int k=l;

    while(i<leftArraySize && j<rightArraySize){
        if(leftArray[i] < rightArray[j]){
            arr[k] = leftArray[i];
            i++;
        } else {
            arr[k] = rightArray[j];
            j++;
        }
        k++;
    }

    while(i<leftArraySize){
        arr[k] = leftArray[i];
        i++;
        k++;
    }

    while(j<rightArraySize){
        arr[k] = rightArray[j];
        j++;
        k++;
    }
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int left, int right) 
{ 
    if(left>=right){ return;}
    int m = (left+right)/2;
    
    mergeSort(arr, left, m);
    mergeSort(arr, m+1, right);
    
    merge(arr, left, m, right);

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
    //int arr[] = {12, 11, 13, 5, 6, 7}; 
    int arr[] = {12, 11,9, 8, 6, 5, 2, 1, 0}; 
    int arr_size = sizeof(arr)/sizeof(arr[0]); 
  
    printf("Given array is \n"); 
    printArray(arr, arr_size); 
  
    mergeSort(arr, 0, arr_size - 1); 
  
    printf("\nSorted array is \n"); 
    printArray(arr, arr_size); 
    return 0; 
}