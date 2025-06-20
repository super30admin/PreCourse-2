// Time Complexity :O(logn)
// Space Complexity :O(1)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :
//First we need to check if the array is sorted or not.
//if the array is not sorted then just use normal linear search which take O(n) time.
//because sorting time of an array is O(nlogn ) and after that binary search is O(logn).

// Your code here along with comments explaining your approach


#include <stdio.h> 
#include <limits.h>
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 

int isAscArray(int arr[], int highindex){
    for(int i=0; i < highindex; i++){ //check till highindex-1 only 
        if(arr[i] > arr[i+1]){
            return -1;
        }        
    }
    return 0;
}

int binarySearch(int arr[], int l, int r, int x) 
{   
    if(r >=l){

        int mid = l + ((r - l)/2);
       
        if(arr[mid] == x){  //checking mid
            return mid;
        }
        else if(arr[mid] > x){
            return binarySearch(arr, l, mid - 1, x);  // considering left array   as array is in ascending order 
        }
        else{
            return binarySearch(arr, mid + 1, r, x);  //considering right array
        }
    }
    else{
        printf("input paramets are wrong\n");
        return INT_MIN;
    }
    return -1;
} 
  
int main(void) 
{ 
    int arr[] = { 2, 3, 4, 40, 10 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    int x = 10; 

    if(isAscArray(arr, n -1) == -1){
        printf("Array is not in ascending order\n");  //checking if the array is in ascending order, or sorted 
        return INT_MIN;
    }

    int result = binarySearch(arr, 0, n - 1, x);
    (result == -1) ? printf("Element is not present in array\n") 
                   : printf("Element is present at index %d\n", 
                            result); 
    return 0; 
} 