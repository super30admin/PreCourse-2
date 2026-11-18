// Time: O(log n); Space: O(log n) for the recursive call stack

#include <cstdio>

// Return the index of x in sorted arr[l..r], or -1 when it is absent.
int binarySearch(int arr[], int l, int r, int x)
{
    if (l > r) {
        return -1;
    }

    int mid = l + (r - l) / 2;
    if (arr[mid] == x) {
        return mid;
    }
    if (arr[mid] < x) {
        return binarySearch(arr, mid + 1, r, x);
    }
    return binarySearch(arr, l, mid - 1, x);
}

int main(void)
{
    int arr[] = {2, 3, 4, 10, 40};
    int n = sizeof(arr) / sizeof(arr[0]);
    int result = binarySearch(arr, 0, n - 1, 10);
    if (result == -1) {
        std::printf("Element is not present in array");
    } else {
        std::printf("Element is present at index %d", result);
    }
    return 0;
}
