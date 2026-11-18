// Time: O(n log n); Space: O(n)

#include <iostream>
#include <vector>

// Merge the already sorted ranges arr[l..m] and arr[m+1..r].
void merge(int arr[], int l, int m, int r)
{
    std::vector<int> merged;
    merged.reserve(r - l + 1);
    int left = l;
    int right = m + 1;

    // Taking from the left on ties keeps the sort stable.
    while (left <= m && right <= r) {
        merged.push_back(arr[left] <= arr[right] ? arr[left++] : arr[right++]);
    }
    while (left <= m) {
        merged.push_back(arr[left++]);
    }
    while (right <= r) {
        merged.push_back(arr[right++]);
    }
    for (int i = 0; i < static_cast<int>(merged.size()); ++i) {
        arr[l + i] = merged[i];
    }
}

void mergeSort(int arr[], int l, int r)
{
    if (l < r) {
        int middle = l + (r - l) / 2;
        mergeSort(arr, l, middle);
        mergeSort(arr, middle + 1, r);
        merge(arr, l, middle, r);
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
    int arr[] = {12, 11, 13, 5, 6, 7};
    int size = sizeof(arr) / sizeof(arr[0]);
    std::cout << "Given array is\n";
    printArray(arr, size);
    mergeSort(arr, 0, size - 1);
    std::cout << "\nSorted array is\n";
    printArray(arr, size);
    return 0;
}
