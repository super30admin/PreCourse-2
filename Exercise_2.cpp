#include <bits/stdc++.h> 
using namespace std;  
  
// A utility function to swap two elements  
void swap(int* a, int* b)  
{  
    //Your Code here
    int temp = *b;
    *b = *a;
    *a = temp; 
}  
  
/* This function takes last element as pivot, places  
the pivot element at its correct position in sorted  
array, and places all smaller (smaller than pivot)  
to left of pivot and all greater elements to right  
of pivot */

int partition (int arr[], int low, int high)  
{  
    //Your Code here 
    
    // Index of first element as m.
    int m = low;

    // Last element as pivot.
    int pivot = arr[high];
 
    for (int n = low; n < high ; n++)
    {
        // If pivot is greater than current element.
        if (arr[n] < pivot)
        {
            swap(&arr[m], &arr[n]);

            // Increment index of smaller element.
            m++;
        }
    }
    swap(&arr[m], &arr[high]);
    return m;
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */

// Time Complexity : O(nlogn). When the input array is sorted or nearly sorted,
// the time complexity with last element as pivot becomes O(n^2).
// Space Complexity : O(1) 
void quickSort(int arr[], int low, int high)  
{  
    //Your Code here
    if (low < high)
    {
        // par_index is the index at which partitioning occurs.
        int par_index = partition(arr, low, high);
 
        // Sort elements before partition and after partition.
        quickSort(arr, low, par_index - 1);
        quickSort(arr, par_index + 1, high);
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