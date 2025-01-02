// #include <bits/stdc++.h>
#include <iostream>

using namespace std;

// A utility function to swap two elements
void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

/* This function takes the last element as pivot, places
   the pivot element at its correct position in the sorted
   array, and places all smaller elements to the left of
   pivot and all greater elements to the right of pivot */
int partition(int arr[], int low, int high)
{
    int pivot = arr[high]; // Pivot element
    int i = low - 1;       // Index of smaller element

    for (int j = low; j < high; j++) {
        // If the current element is smaller than or equal to the pivot
        if (arr[j] <= pivot) {
            i++; // Increment the index of the smaller element
            swap(&arr[i], &arr[j]);
        }
    }

    // Swap the pivot element with the element at index i+1
    swap(&arr[i + 1], &arr[high]);
    return i + 1; // Return the partitioning index
}

/* The main function that implements QuickSort
   arr[] --> Array to be sorted,
   low  --> Starting index,
   high --> Ending index */
void quickSort(int arr[], int low, int high)
{
    if (low < high) {
        // Partition the array around the pivot
        int pi = partition(arr, low, high);

        // Recursively sort elements before and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
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
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    quickSort(arr, 0, n - 1);
    cout << "Sorted array: \n";
    printArray(arr, n);
    return 0;
}
