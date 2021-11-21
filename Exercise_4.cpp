#include<stdlib.h> 
#include<stdio.h> 
#include<iostream>
  
// Time Complexity : O(n log n) 
// Space Complexity : O(n) Need extra space of similar size as input array.
// Any problem you faced while coding this : Had to take extra array. Could not sort inplace

void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int sizeL = m - l + 1;
    int sizeR = r - m;
    int *LArray,*RArray;

    LArray = new int[sizeL];
    RArray = new int[sizeR];

    for(int i = 0; i < sizeL; i++)
    {
        LArray[i] = arr[l + i];
    }

    for(int i = 0; i < sizeR; i++)
    {
        RArray[i] = arr[m + 1 + i];
    }

    int leftPointer = 0;
    int rightPointer = 0;

    int arrayIndex = l;

    while(leftPointer < sizeL && rightPointer < sizeR)
    {
        if(LArray[leftPointer] < RArray[rightPointer])
        {
            arr[arrayIndex] = LArray[leftPointer];
            leftPointer++;
        }
        else
        {
            arr[arrayIndex] = RArray[rightPointer];
            rightPointer++;
        }
        arrayIndex++;
    }

    while(leftPointer < sizeL)
    {
        arr[arrayIndex] = LArray[leftPointer];
        arrayIndex++;
        leftPointer++;
    }

    while(rightPointer < sizeR)
    {
        arr[arrayIndex] = RArray[rightPointer];
        arrayIndex++;
        rightPointer++;
    }

    delete LArray;
    delete RArray;
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
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if(r > l)
    {
        int mid = (l + r) / 2;

        mergeSort(arr, l , mid);
        mergeSort(arr, mid + 1, r);

        merge(arr, l , mid , r);
    }
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