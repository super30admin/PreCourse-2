#include <stdio.h> 
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1

// Time Complexity : O(log n)
// Space Complexity : O(1)
int binarySearch(int arr[], int l, int r, int x) 
{   
    //Your Code here 
    if (l <= r) {
        int mid = (l + r) / 2;
 
        // If the element matches the middle element, return its index.
        if (arr[mid] == x)
            return mid;
 
        // If element is greater than mid, then it can
        // be present in right part of the array.
        if (arr[mid] < x)
            return binarySearch(arr, mid + 1, r, x);
 
        // If element is smaller than mid, then it can
        // be present in left part of the array.
        return binarySearch(arr, l, mid - 1, x);
    }

    // If the element is not present in the array, return -1.
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