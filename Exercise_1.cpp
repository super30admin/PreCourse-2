// Time Complexity : O(logn) for sorted array
// Space Complexity : O(1) as no extra space is used
// Did this code successfully run on Leetcode : 
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach

#include <stdio.h> 
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{   
    //Your Code here 
    if (l<=r) { 
        int mid = l + (r - l) / 2; 
  
        // If the element is present at the middle itself 
        if (arr[mid] == x) 
            return mid; 
  
        // If element is smaller than mid, then it can only be present in left subarray 
        if (arr[mid] > x) 
            return binarySearch(arr, l, mid - 1, x); 
  
        // Else the element can only be present in right subarray 
        return binarySearch(arr, mid + 1, r, x); 
    }
    return -1; //Element not found
} 
  
int main(void) 
{ 
    int arr[] = { 2, 3, 4, 10, 40 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    int x = 50; 
    int result = binarySearch(arr, 0, n - 1, x); 
    (result == -1) ? printf("Element is not present in array") 
                   : printf("Element is present at index %d", 
                            result); 
    return 0; 
} 