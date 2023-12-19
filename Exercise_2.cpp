// Time Complexity : O(NlogN)
// LogN as we are divided the array into two halves,
// pivot placement each time for N elements
// Space Complexity : O(N)
// Recursion Call Stack

#include <bits/stdc++.h>
using namespace std;

// A utility function to swap two elements
void swap(int *a, int *b)
{
    // Your Code here
    int *temp = a;
    a = b;
    b = temp;
}

/* This function takes last element as pivot, places
the pivot element at its correct position in sorted
array, and places all smaller (smaller than pivot)
to left of pivot and all greater elements to right
of pivot */
int partition(int arr[], int low, int high)
{
    // Your Code here
    int pivot = arr[high], start = low - 1, end = low;

    // check till end reach last but one index
    while (end < high)
    {
        // if element is less than equal to pivot,
        // we have to swap the element
        if (arr[end] <= pivot)
        {
            // as start in below low, increment and swap
            start++;

            swap(arr[start], arr[end]);
        }

        end++;
    }

    // once end reaches the last but one index,
    // correct position of pivot is found at start+1
    // swap the pivot with start+1
    start++;

    swap(arr[start], arr[high]);

    // return the pivot index
    return start;
}

/* The main function that implements QuickSort
arr[] --> Array to be sorted,
low --> Starting index,
high --> Ending index */
void quickSort(int arr[], int low, int high)
{
    // Your Code here
    int paritionIndex;

    if (low < high)
    {
        // place the right most element at correct position
        // and returns the index of the element 
        paritionIndex = partition(arr, low, high);

        // As partition element is at right place,
        // sort the left half individually
        quickSort(arr, low, paritionIndex - 1);

        // sort the right half individually
        quickSort(arr, paritionIndex + 1, high);
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