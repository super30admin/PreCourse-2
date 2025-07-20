#include <stdio.h> 
//Time Complexity : O(logn)
//Space Complexity : O(1)  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{   
    //Your Code here 
    if(r>=l){
        int mid=l+(r-l)/2;//middle location in the array

        if(arr[mid]==x)//if the element and the mid value of array are equal
            return mid;//return the value of mid
        
        if(arr[mid]>x)//If x is smaller than the middle value
            return binarySearch(arr,l,mid-1,x);
            //then x will be in the left side of the array
        return binarySearch(arr,mid+1,r,x);//or it will be in the right of array
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