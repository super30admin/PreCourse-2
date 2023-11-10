#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r)              
{ 
    //Your code here
    int k =0;

    int lenFirstHalf=m-l;


    int left[m-l];
    int startOfFirstHalf=l;
    for(int i=0;i<m-l;i++)
    {
        left[i]=arr[startOfFirstHalf];
        startOfFirstHalf++;
    }

    int right[r-m+1];
    int startOfSecondHalf=m+1;

    for(int j=0;j<r-m+1;j++)
    {
        right[j]=arr[m+1];
        m++;
    }


    int lenSecondHalf=r-startOfSecondHalf;

    while(l<=lenFirstHalf && startOfSecondHalf<=lenSecondHalf)
    {
        
    }
    while(l<=lenFirstHalf)
    {
        arr[k]=arr[l];
        k++;
        l++;
    }
    while(startOfSecondHalf<=lenSecondHalf)
    {
        arr[k]=arr[startOfSecondHalf];
        k++;
        startOfSecondHalf++;
    }
    
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if(l == r)
    {
        return;
    }
    int midIndex=l+((r-l)/2);
    mergeSort(arr,l,midIndex);
    mergeSort(arr,midIndex+1,r);
    merge(arr,l,midIndex,r);

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