// Time: O(n log n) average, O(n^2) worst; Space: O(log n) average recursion

#include <iostream>

// Lomuto partition: move values <= pivot to its left.
int partition(int arr[], int low, int high)
{
    int pivot = arr[high];
    int boundary = low - 1;
    for (int current = low; current < high; ++current) {
        if (arr[current] <= pivot) {
            ++boundary;
            int value = arr[boundary];
            arr[boundary] = arr[current];
            arr[current] = value;
        }
    }
    int value = arr[boundary + 1];
    arr[boundary + 1] = arr[high];
    arr[high] = value;
    return boundary + 1;
}

// Sort arr[low..high] in place.
void quickSort(int arr[], int low, int high)
{
    if (low < high) {
        int pivotIndex = partition(arr, low, high);
        quickSort(arr, low, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, high);
    }
}

void printArray(int arr[], int size)
{
    for (int i = 0; i < size; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << '\n';
}

int main()
{
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    quickSort(arr, 0, n - 1);
    std::cout << "Sorted array:\n";
    printArray(arr, n);
    return 0;
}
