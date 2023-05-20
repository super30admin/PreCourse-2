#include <bits/stdc++.h> 
using namespace std;

// A utility function to swap two elements

// Time Complexity: O(1)
// Space Complexity: O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
void swap(int* a, int* b)
{
    // Swapping the values of two variables
    int temp = *a;
    *a = *b;
    *b = temp;
}

/* This function takes the last element as pivot, places
the pivot element at its correct position in the sorted
array, and places all smaller (smaller than pivot)
to the left of the pivot and all greater elements to the right
of the pivot */
// Time Complexity: O(n)
// Space Complexity: O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : choosing the correct element for swapping function
int partition(int arr[], int low, int high)
{
    // Choosing the last element as the pivot
    int pivot = arr[high];
    int i = (low - 1); // Index of the smaller element

    for (int j = low; j <= high - 1; j++) {
        // If the current element is smaller than the pivot
        if (arr[j] < pivot) {
            i++; // Increment the index of the smaller element
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

/* The main function that implements QuickSort
arr[] --> Array to be sorted,
low --> Starting index,
high --> Ending index */
// Time Complexity: O(n^2)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
// Space Complexity: O(1)
void quickSort(int arr[], int low, int high)
{
    // Base case: If low is less than high
    if (low < high) {
        // Partition the array
        int pi = partition(arr, low, high);

        // Recursively sort the subarrays
        quickSort(arr, low, pi - 1); // Before the pivot
        quickSort(arr, pi + 1, high); // After the pivot
    }
}

/* Function to print an array */
void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

// Driver Code
int main()
{
    int arr[] = { 10, 7, 8, 9, 1, 5 };
    int n = sizeof(arr) / sizeof(arr[0]);
    quickSort(arr, 0, n - 1);
    cout << "Sorted array: \n";
    printArray(arr, n);
    return 0;
}
