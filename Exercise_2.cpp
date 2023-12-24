/*
-------------------------------------
* Recursive Quick Sort Implememtation
-------------------------------------

* Time Complexity:
*        - Average Case: O(nlog(n))
*        - Worst Case: O(n^2)

* Space Complexity: O(n)

Did this code successfully run on Leetcode : NA
Any problem you faced while coding this : NO

*/

#include <iostream>

// A utility function to swap two elements
void swap(int* a, int* b)
{
    //Your Code here
    int temp = *a;
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
    // Always picking the first element as the pivot
    int pivot_element = arr[low];
    int start = low, end = high;

    while (start < end) {
        // Find left most element greater than or equal to the pivot element
        while (start < end && arr[start] <= pivot_element)
            start++;
        // Find right most element less than or equal to the pivot element
        while (arr[end] > pivot_element)
            end--;

        if (start < end)
            swap(&arr[start], &arr[end]);
    }
    // Swap pivot element with the last element
    swap(&arr[low], &arr[end]);
    return end;
}

/* The main function that implements QuickSort
arr[] --> Array to be sorted,
low --> Starting index,
high --> Ending index */
void quickSort(int arr[], int low, int high)
{
    // Base case
    if (low >= high)
        return;

    // Partition the array
    int p = partition(arr, low, high);

    // Sort the left side
    quickSort(arr, low, p - 1);

    // Sort the right side
    quickSort(arr, p + 1, high);

}

/* Function to print an array */
void printArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        std::cout << arr[i] << " ";
    std::cout << std::endl;
}

// Driver Code
int main()
{
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    quickSort(arr, 0, n - 1);
    std::cout << "Sorted array: \n";
    printArray(arr, n);
    return 0;
}