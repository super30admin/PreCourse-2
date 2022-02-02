// Time Complexity : O(log(n))
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : No

#include <stdio.h> 
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{   
    if(r >= l){
        int m = (l + r - 1)/2;

        if(x == arr[m])
            return m;
        else if(x > arr[m])
            return binarySearch(arr[], m+1, r, x);
        else
            return binarySearch(arr[], l, m-1, x);
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