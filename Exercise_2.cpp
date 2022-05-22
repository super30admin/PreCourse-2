// Time Complexity - I was unable to visualize what the time comlexity would be here for partition() and the quicksort().
// Problems faced - Sometimes my program fails to build. I tried to figure it out but could not understand why it was happening.
// I was getitng a stack buffer underflow error.

#include <bits/stdc++.h>
using namespace std;
  
// A utility function to swap two elements
void swap(int* a, int* b)
{
    //Your Code here
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
  
/* This function takes last element as pivot, places
the pivot element at its correct position in sorted
array, and places all smaller (smaller than pivot)
to left of pivot and all greater elements to right
of pivot */
int partition (int arr[], int low, int high)
{
    //Your Code here
    int pivot = arr[high];
    int i = low; // left pointer
    int j = high; // right pointer
    
    // left pointer checks for elements greater than or equal to pivot. It stops as soon as it finds one.
    // right pointer checks for elements less than pivot. It stops as soon as it finds one.
    // if their search is successfull and at that point i is less than j, I swap those elements
    // if i > j it breaks out of the while loop and swaps pivot and arr[i]
    while(i < j){
        while(arr[i] < pivot)
            i++;
        do{
            j--;
        }while(arr[j] >= pivot);
        
        if(i < j)
            swap(&arr[i], &arr[j]);
    }
    
    swap(&arr[high], &arr[i]);
    return i;
}
  
/* The main function that implements QuickSort
arr[] --> Array to be sorted,
low --> Starting index,
high --> Ending index */
void quickSort(int arr[], int low, int high)
{
    //Your Code here
    if(low < high){
        int index = partition(arr, low, high);
        quickSort(arr, low, index-1);
        quickSort(arr, index+1, high);
    }
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
    int arr[] = {10, 7, 8, -90, 121, 23, 1234, 45, 20, 0};
    int n = sizeof(arr) / sizeof(arr[0]);
    quickSort(arr, 0, n - 1);
    cout << "Sorted array: \n";
    printArray(arr, n);
    return 0;
}
