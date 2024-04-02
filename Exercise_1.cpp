//
//TIME Complexity: O(log n)
//SPACE Complexity: O(n)
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
#include <stdio.h> 
int binarySearch(int arr[], int l, int r, int x) 
{   
   
   int mid = 0;
    
   while(l<=r) {
        mid = l + (r-l)/2;
        if(arr[mid] == x) {
            return mid;
        } else if(x < arr[mid]) {
            r = mid - 1;
        } else {
            l = mid + 1;
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
    (result == -1) ? printf("Element is not present in array \n") 
                   : printf("Element is present at index %d \n", 
                            result); 
    x = 5; 
    result = binarySearch(arr, 0, n - 1, x); 
    (result == -1) ? printf("Element is not present in array \n") 
                   : printf("Element is present at index %d \n", 
                            result);
    x = 40; 
    result = binarySearch(arr, 0, n - 1, x); 
    (result == -1) ? printf("Element is not present in array \n") 
                   : printf("Element is present at index %d \n", 
                            result); 
    
    return 0; 
} 
