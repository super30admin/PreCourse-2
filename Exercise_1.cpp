/**
 * Time complexity:
 * O(logn)
 */

/**
 * Space Complexity:
 * The space complexity is O(1) as we are not creating any extra space.
 * 
 */

/**
 * Approach: 
 * The entire sorted array is our search space. In binary search we repeatedly
 * divide the search space in half. If the value we have to find is less than
 * the element in the middle we will reduce the search space to the left half.
 * Otherwise, the search space will be reduced to right half.
 * 
 */

// The code ran perfectly



#include <stdio.h> 
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{   
    //Your Code here 
    
    while(l<r){
        int mid  =  l + (r -l)/2;
        if(arr[mid] == x) return mid;
        if(arr[mid] > x){
            return binarySearch(arr, l, mid, x);
        } 
        if(arr[mid] < x){
            return binarySearch(arr, mid +1, r, x);
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