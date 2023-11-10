#include <stdio.h> 
  
//Time complexity = O(log(n))
//Space complexity = O(n)
int binarySearch(int arr[], int l, int r, int x) 
{   
    //Check to make sure array size is atleast 1. If it is less than one, it means that the element was not found.//
    if (r >= l)
    {
        int mid = (l + r) / 2;

        if (arr[mid] == x)  //Base case
            return mid;

        if (arr[mid] > x)   //Searching upper half of the array
            return binarySearch(arr, l, mid - 1, x);

        else   //Searching lower half of the array
            return binarySearch(arr, mid + 1, r, x);
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