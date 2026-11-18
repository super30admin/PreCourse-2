// Time: O(n log n) average, O(n^2) worst; Space: O(n) explicit range stack

#include <iostream>
#include <utility>
#include <vector>

int partition(int arr[], int l, int h)
{
    int pivot = arr[h];
    int boundary = l - 1;
    for (int current = l; current < h; ++current) {
        if (arr[current] <= pivot) {
            ++boundary;
            std::swap(arr[boundary], arr[current]);
        }
    }
    std::swap(arr[boundary + 1], arr[h]);
    return boundary + 1;
}

// Store pending ranges in a vector instead of using recursive calls.
void quickSortIterative(int arr[], int l, int h)
{
    if (l >= h) {
        return;
    }

    std::vector<std::pair<int, int>> ranges;
    ranges.emplace_back(l, h);
    while (!ranges.empty()) {
        auto [low, high] = ranges.back();
        ranges.pop_back();
        int pivotIndex = partition(arr, low, high);
        if (low < pivotIndex - 1) {
            ranges.emplace_back(low, pivotIndex - 1);
        }
        if (pivotIndex + 1 < high) {
            ranges.emplace_back(pivotIndex + 1, high);
        }
    }
}

void printArr(int arr[], int n)
{
    for (int i = 0; i < n; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << '\n';
}

int main()
{
    int arr[] = {4, 3, 5, 2, 1, 3, 2, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    quickSortIterative(arr, 0, n - 1);
    printArr(arr, n);
    return 0;
}
