// TC: O(log n), since we reduce the search space by half each time. So for an array of size 8, we would call the function 4 times in the worst
// case: 8 -> 4 -> 2 -> 1. log(8) with base 2 = 3 (roughly equal to 4). Therefore, the TC is O(log n).
// SC: O(log n), since there are log n recursive calls, the recursion stack will have size O(log n). We can optimize this to O(1) space complexity
// by using an iterative approach.
// Explanation in Sample.java

#include<bits/stdc++.h>  
using namespace std;

// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{   
    //Your Code here 
    if(l>r) return -1;
    int mid = l + (r-l)/2; // to avoid integer overflow
    if(arr[mid] == x) return mid; // found the search element
    else if(arr[mid] > x) return binarySearch(arr, l, mid-1, x); // element possibly exists in the left half
    else return binarySearch(arr, mid+1, r, x); // element possibly exists in the right half  
} 

// iterative approach
int binarySearchIter(int arr[], int l, int r, int x) {
    while(l<=r) {
        int mid = l + (r-l)/2; 
        if(arr[mid] == x){ 
            return mid;
        } else if(arr[mid] < x) {
            l = mid + 1;
        } else{
             r = mid - 1;
        }
    }
    return -1;
}

bool isSorted(int A[], int size) {
    for(int i=1; i<size; i++){
        if(A[i-1] > A[i]) return false;
    }
    return true;
}

int main(void) 
{ 
    /* TEST CASES */
    int arr[] = { 2, 3, 4, 10, 40 }; int x = 15; // not present
    // int arr[] = {5}; int x = 4; // single element
    // int arr[] = {1, 3, 2, 5, 0}; int x = 3; // unsorted 
    // int arr[] = {}; int x = 5; // empty
    // int arr[] = {2, 2, 2, 2, 2}; int x = 2;   // all duplicates
    // int arr[] = {-10, -3, 0, 1, 8}; int x = -3;   // negative
    // int arr[] = {INT_MIN, -1, 0, 1, INT_MAX}; int x = INT_MIN;   // extreme values

    int n = sizeof(arr) / sizeof(arr[0]); 
    if(n <= 0) {
        cerr<<"Invalid array"<<endl;
        return 0;
    }
    if(!isSorted(arr, n)){
        cerr<<"Binary search requires sorted array!"<<endl;
        return 0;
    }
    int result = binarySearchIter(arr, 0, n - 1, x); 
    (result == -1) ? printf("Element is not present in array") 
                   : printf("Element is present at index %d", 
                            result); 
    return 0; 
} 