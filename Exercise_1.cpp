#include <stdio.h>

// Time Complexity : O(log n)
// Space Complexity : O(log n) // Recursive stack space

// A recursive binary search function. It returns 
// location of x in given array arr[low..r] is present,
// otherwise -1 
int binarySearch(int arr[], int low, int high, int x)
{
    //Your Code here 
    if(high >= low){
        int mid = low + (high - low) / 2;
        if(arr[mid] == x) return mid;
        else if(arr[mid] > x) return binarySearch(arr, low, mid - 1, x);
        else if(arr[mid] < x) return binarySearch(arr, mid + 1, high, x);
    }
    return -1;
}

int main(void)
{
    int arr[] = { 2, 3, 4, 10, 40 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;
    int result = binarySearch(arr, 0, n - 1, x);
    (result == -1) ? printf("Element is not present in array")
                   : printf("Element is present at index %d",
                            result);
    return 0;
} 