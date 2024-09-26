#include <stdio.h> 
#include<iostream>
#include<math.h>

using namespace std;
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{   
    //Get the Mid Point
    int m = floor((l + r) / 2);
    
    //Found the element
    if(arr[m] == x)
    {
        return m;
    }
    //Smaller element
    else if(x < arr[m])
    {
        return binarySearch(arr, l, m, x);
    }
    //Larger element
    else
    {
        return binarySearch(arr,m+1, r, x);
    }
    
    cout << "\nShouldn't come here" << endl;
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

/**
 * @brief Complexity Analysis
 * Time - O(logn)
 * Space - In-place
 */