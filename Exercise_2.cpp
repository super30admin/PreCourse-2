#include <bits/stdc++.h> 
using namespace std;  

/*
Time Complexity :
    quicksort(): O(nlogn), n is the number of elements in the array

Space Complexity : O(1) - no extra set of datastructure used

Did this code successfully run on Leetcode : Couldn't find the leetcode problem

Any problem you faced while coding this : None
*/

// A utility function to swap two elements  
void swap(int* a, int* b)  
{  
    int temp = *a;

    a = b;
    *b = temp;

}  
  
/* This function takes last element as pivot, places  
the pivot element at its correct position in sorted  
array, and places all smaller (smaller than pivot)  
to left of pivot and all greater elements to right  
of pivot */
int partition (int arr[], int low, int high)  
{  
    int pivot = arr[high];

    int i = low;

    for (int j = low;j < high;j ++) {
        if (arr[j] <= pivot) {
            swap(arr[i], arr[j]);
            i ++;
        }
    }

    swap(arr[i], arr[high]);
    return i;
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
    if (low < high) {
        int part = partition(arr, low, high);

        quickSort(arr, low, part - 1);
        quickSort(arr, part + 1, high);
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
    int arr[] = {10, 7, 8, 9, 1, 5};  
    int n = sizeof(arr) / sizeof(arr[0]);  
    quickSort(arr, 0, n - 1);  
    cout << "Sorted array: \n";  
    printArray(arr, n);  
    return 0;  
}  