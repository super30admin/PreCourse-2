#include <stdio.h> 
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 

// Time Complexity : O(log n) because array size for each function call is divided in half. 
// Space Complexity : O(1) constant space.
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No


int binarySearch(int arr[], int l, int r, int x) 
{   
    //Your Code here 
    int mid = (l + r) / 2;
    int finalVal = -1;
    if(arr[mid] == x)
    {
        finalVal = mid;
    }

    if((x > arr[mid]) && ((mid + 1) <= r))
    {
       finalVal = binarySearch(arr, mid + 1 , r , x);
    }

    if((x < arr[mid]) && ((mid - 1) >= l))
    {
        finalVal = binarySearch(arr, l , mid - 1, x);
    }

    return finalVal;
} 
  
int main(void) 
{ 
    int arr[] = { 2, 3, 4, 10, 40 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    int x = 100; 
    int result = binarySearch(arr, 0, n - 1, x); 
    (result == -1) ? printf("Element is not present in array") 
                   : printf("Element is present at index %d", 
                            result); 
    return 0; 
} 