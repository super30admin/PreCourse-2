#include <stdio.h> 
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{   
    //Your Code here 
    int indexMiddleElement= l + (r-l)/2;
    int middleElement=arr[indexMiddleElement];
    if(x==middleElement)
    {
        return indexMiddleElement;
    }

    if(r<=l)
    {
        return -1;
    }
    if(x>middleElement)
    {
        return binarySearch(arr,indexMiddleElement+1,r,x);
    }
    return binarySearch(arr,l,indexMiddleElement-1,x);
} 
  
int main(void) 
{ 
    int arr[] = { 2, 3, 4, 10, 40 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    int x = 10; 
    int result = binarySearch(arr, 0, n - 1, 30); 
    (result == -1) ? printf("Element is not present in array") 
                   : printf("Element is present at index %d", 
                            result); 
    return 0; 
} 