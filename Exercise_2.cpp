/*

TC: O(n2) worst case, O(nlgn) avg case
SC: O(1)
Logic: 
1. Partition the array around a pivot in O(n) using the partition method consisting of simple swaps
2. let quicksort sort the elements around the partition element, ie. recurse for left of the partition and right.

*/

#include <iostream>
#include <bits/stdc++.h> 
using namespace std;  
  
// A utility function to swap two elements  
void swap(int* a, int* b)  
{  
    int temp=*a;
    *a=*b;
    *b=temp;
}  
  
/* This function takes last element as pivot, places  
the pivot element at its correct position in sorted  
array, and places all smaller (smaller than pivot)  
to left of pivot and all greater elements to right  
of pivot */
int partition (int arr[], int low, int high)  
{  
    int pivot = arr[high];
    int i = low-1;
    for(int j=low; j<high; j++)    
        if(arr[j] < pivot)  i++, swap(&arr[i], &arr[j]);
    swap(&arr[i+1], &arr[high]);
    return i+1;
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
    if(low > high)  return;
    int pi = partition(arr, low, high);
    quickSort(arr, low, pi-1);
    quickSort(arr, pi+1, high);
}  
  
/* Function to print an array */
void printArray(int arr[], int size)  
{  
    int i;  
    for (i = 0; i < size; i++)  
        cout << arr[i] << " ";  
    cout << endl;  
}  
  
// Driver Code 
int main()  
{  
    int arr[] = {10, 7, 8, 9, 1, 5};  
    int n = sizeof(arr) / sizeof(arr[0]);  
    quickSort(arr, 0, n - 1);  
    cout << "Sorted array: \n";  
    printArray(arr, n);  
    return 0;  
}  