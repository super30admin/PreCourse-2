/*

TC: O(lgn)
SC: O(1)
Logic: 
1. we split the sorted array in the middle
2. if target == current mid, then boom! we found it, so simply return
3. if target > current mid, then clearly we'd find the element in the right side, so we recurse for the right end. Similarly for the left end.

*/
#include <stdio.h> 
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{   
    if(l>r) return -1;
    int mid = l+(r-l)/2;
    if(arr[mid] == x)   return mid;
    else if(x < arr[mid])   return binarySearch(arr, l, mid-1, x);
    else    return binarySearch(arr, mid+1, r, x);
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