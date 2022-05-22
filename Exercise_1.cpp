// Time-Complexity -> For a sorted array we know that Binary search takes O(log n). "n" is the number of elements in the array.

// Problems Faced - No!

#include <stdio.h>
  
// A recursive binary search function. It returns
// location of x in given array arr[l..r] is present,
// otherwise -1
int binarySearch(int arr[], int l, int r, int x)
{
    //Your Code here
    // We check if the left index is less than or equal to right index. If it is, we recursively call the Binary search method on the left half or the right half based on the value we are searching.
    // If we are unable to find the lement we return -1.
    if(l <= r){
        int middle = l + (r-l)/2;
        if(arr[middle] == x)
            return middle;
        else if(arr[middle] < x)
            return binarySearch(arr, (middle + 1), r, x);
        else if(arr[middle] > x)
            return binarySearch(arr, l, (middle - 1), x);
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
