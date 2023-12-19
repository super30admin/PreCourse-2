// Time Complexity : O(logN)
        // each time search space is divided by half.
// Space Complexity : O(1)
        // no extra space

#include <stdio.h>

// A recursive binary search function. It returns
// location of x in given array arr[l..r] is present,
// otherwise -1
int binarySearch(int arr[], int l, int r, int x)
{
    // Your Code here
    int mid;

    // iterating till left and right pointer cross each other
    while (l <= r)
    {
        // calculate the mid point
        mid = l + ((r - l) / 2);

        // check if middle element is equal to x
        if (arr[mid] == x)
            return mid;

        // if middle element is less than x, eliminate left search space
        else if (arr[mid] < x)
            l = mid + 1;

        // if middle element is greater than x, eliminate right search space
        else
            r = mid - 1;
    }

    // if element not found
    return -1;
}

int main(void)
{
    int arr[] = {2, 3, 4, 10, 40};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;
    int result = binarySearch(arr, 0, n - 1, x);
    (result == -1) ? printf("Element is not present in array")
                   : printf("Element is present at index %d",
                            result);
    return 0;
}