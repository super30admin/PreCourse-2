// Time Complexity : O(log N). best case O(1)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : I made a logical mistake.

// Your code here along with comments explaining your approach


#include <stdio.h> 
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{   
    //Your Code here 
    int middle = 0;
    
    while(l<=r){
        middle = int((l+r)/2); // I took int() because if value of l+r is odd, then we'll get a fraction.
        
        if(arr[middle]==x){ //checking if x is equal to middle, if yes then we can stop the search here. best case.
            return middle;
        }
        
        else if(arr[middle]>x){ //else we must reduce the size of the array by half and repeat the above two steps.
            r = middle-1;
        }
        else{
            l = middle+1;
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