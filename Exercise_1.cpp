// Time Complexity : O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : -
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach
//find the middle element by diving the low and high divided by 2, check if it's equal to the target, if yes then return the middle element index
//else if the middle element is lesser than the target, then move low to mid+1 and do binary search again
//else move high to mid-1 and do binary search
//if the target is not found, return -1

#include <stdio.h> 
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{   
    //Your Code here 
    while(l<=r){
        int mid = l + (r-l)/2;
        if(arr[mid] == x){
            return mid;
        }
        else if(arr[mid] < x){
            l = mid+1;
        }
        else{
            r = mid-1;
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