#include<bits/stdc++.h>
using namespace std; 
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int a[], int l, int r, int x) 
{   
    //Your Code here
    if(l <= r) {
        int m = l + (r - l) / 2;
        if(a[m] == x) {
            return m;
        } else if(a[m] < x) {
            return binarySearch(a, m+1, r, x);
        } else {
            return binarySearch(a, l, m-1, x);
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