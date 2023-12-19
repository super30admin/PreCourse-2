// Time Complexity : O(n^2)
// Space Complexity : O(n) stack space
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :
#include <bits/stdc++.h>
using namespace std;

// A utility function to swap two elements
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

/* This function takes last element as pivot, places
the pivot element at its correct position in sorted
array, and places all smaller (smaller than pivot)
to left of pivot and all greater elements to right
of pivot */
int partition(int arr[], int low, int high)
{
    int pivotVal = arr[high];
    int i = low - 1;
    int j = low;
    int k = high + 1;
    while (j < k)
    {
        if (arr[j] < pivotVal)
        {
            swap(arr[i + 1], arr[j]);
            i++;
            j++;
        }
        else if (arr[j] > pivotVal)
        {
            swap(arr[j], arr[k - 1]);
            k--;
        }
        else
        {
            j++;
        }
    }
    return i + 1;
}

/* The main function that implements QuickSort
arr[] --> Array to be sorted,
low --> Starting index,
high --> Ending index */
void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        int partIndex = partition(arr, low, high);
        quickSort(arr, low, partIndex-1);
        quickSort(arr, partIndex + 1, high);
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