// Time Complexity :O(log n)
// Space Complexity :O(1)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach
#include <stdio.h> 
#include <iostream>
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{

    int left = l;
    int right = r;
    int mid = left + (right-left)/2; //optimisation, so it is not effected by integer overflow

    while (left <= right)
    {
        if(arr[mid]==x){ // returns the index of x
            return mid;
        }
        else if (x<arr[mid])  // if x is lesser than the element at the middle index, then the left index will remain the same and the right index will be decreased to mid-1
        {
            right = mid-1;
            
        }
        else{
            left = mid+1;   // if x is greater than the element at the middle index, then the right index will remain the same and the left index will be incremented to mid+1
        }

        mid = left+(right-left)/2; // update the value of mid after each iteration when x not found
        
    }

    return -1; // return -1 if x doesn't exist in the arr[] array
       

     
} 
  
int main(void) 
{ 
    int arr[] = { 2, 3, 4, 10, 40 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    int x = 10; 
    int result = binarySearch(arr, 0, n - 1, x); 
    (result == -1) ? printf("Element is not present in array") 
                   : printf("Element is present at index %d\n", 
                            result); 
    return 0; 
} 