#include <bits/stdc++.h> 
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 

// Time Complexity : O(log n)
// Space Complexity : O(1)

/* Check if the given element is present at the mid of array.
*  If is present then return the mid index.
*  If mid element is less than the target x then search the elemeent between mid index + 1 and R.
*  If mid element is greater than the target x then search the elemeent between L and mid index - 1.
*  If L is greater than r then return -1 as element is not present in array. 
*/
int binarySearch(int arr[], int l, int r, int x) 
{   
    //Your Code here

    if (l > r)
        return -1;

    int mid = (l + r) / 2;

    if (arr[mid] == x)
        return mid;

    if (arr[mid] < x)
        return binarySearch(arr, mid + 1, r, x);

    return binarySearch(arr, l, mid - 1, x);     
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