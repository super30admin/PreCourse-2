// Time Complexity : Log(n)
// Space Complexity : Log(n)
// Any problem you faced while coding this : None.
#include <stdio.h>   
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{   
    if(l>r) return -1; // base condition
    int mid = l + (r-l)/2;   // get the mid of the array
    if(arr[mid] == x) return mid;
    else if(arr[mid] < x)  
    {
        return binarySearch(arr, mid+1, r, x);  // recursively call binarySearch to search element to the right of mid
    }
    else{
        return binarySearch(arr, l, mid-1, x); // recursively call binarySearch to search element to the left of mid
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