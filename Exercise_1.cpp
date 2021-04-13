#include <stdio.h> 


// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{   
    //Time Complexity - O(log n) n being the size of the sorted array.
    //Space Complexity - O(1) Ignoring the space consumed for recursive stacks
    //Searches for an element in a sorted array by dividing it into half over every iteration

    //Your Code here 
    if(l<=r){
        int mid = (l+ r)/2;
        if(arr[mid] == x) return mid;
        else if(arr[mid]<x) return binarySearch(arr, mid+1, r, x);
        else return binarySearch(arr, l, mid-1, x);
    }
    return -1;  
} 
  
int main(void) 
{ 
    int arr[] = { 2, 3, 4, 10, 40 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    int x = 100; 
    int result = binarySearch(arr, 0, n - 1, x); 
    (result == -1) ? printf("Element is not present in array\n") 
                   : printf("Element is present at index %d\n", 
                            result); 
    return 0; 
} 