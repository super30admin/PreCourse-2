
// Time Complexity : O( log(n) ) as each time the array gets divided into half, where n is size of array
// Space Complexity : No extra space complexity other than array provided.
// Any problem you faced while coding this : None

// Your code here along with comments explaining your approach
/* Divide array each time into half where the element can be present as it is sorted array
   and search only in that array*/

#include <iostream> 
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{   
    //Your Code here 
    if( l > r ){
       return -1;
    }
    int mid = ( l + r )/2;
    if( x == arr[mid] ) {
        return mid;
    } else if ( x < arr[mid] ) {
        return binarySearch( arr, l, mid-1, x );
    } else {
        return binarySearch( arr, mid+1, r, x );
    }
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
