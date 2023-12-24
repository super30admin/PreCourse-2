/*
------------------------------------------
* Binary Search Implememtation (Recursive)
------------------------------------------

* Time Complexity: O(log(n))

* Space Complexity: O(log(n))

Did this code successfully run on Leetcode : NA
Any problem you faced while coding this : NO

*/

#include <stdio.h>

// A recursive binary search function. It returns
// location of x in given array arr[l..r] is present,
// otherwise -1
int binarySearch(int arr[], int l, int r, int x) {
    if (l > r) return -1;

    int mid = l + (r - l) / 2; // This equation avoids integer overflow

    if (arr[mid] > x) return binarySearch(arr, l, mid - 1, x);
    else if (arr[mid] < x) return binarySearch(arr, mid + 1, r, x);
    else return mid;
}

int main(void) {
    int arr[] = { 2, 3, 4, 10, 40 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;
    int result = binarySearch(arr, 0, n - 1, x);
    (result == -1) ? printf("Element is not present in array")
                   : printf("Element is present at index %d \n",
                            result);
    return 0;
}