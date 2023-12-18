// Time Complexity : O(logn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : No
#include <stdio.h> 
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{   
    //Your Code here 
    if(arr[l] == x)
    {
        return l;
    }
    while(l<=r)
    {
        int mid = (l+ (r-l)/2);
        if(x == arr[mid])
        {
            return mid;
        }
        else if(x < arr[mid])
        {
            r = mid -1;
        }
        else if(x > arr[mid])
        {
            l = mid+1;
        }
        else{
            // NTD
        }
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