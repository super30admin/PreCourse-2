// Time Complexity : O(n/2) The worst scenario is to get 1st or the last element, n being the length of the array
// Space Complexity :O(n), n being the elements in the array
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach


#include <stdio.h> 
//#include <bits/stdc++.h>
//#include <time.h>
//#include <vector>
//#include <cmath>
//#include <stdlib.h>

// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) //arr[] is array in which we have to search, l is left, r is right and x is the element to be searched in an array
{
    if (r >= 1)
    {
        int middle = l + (r-1)/2;

        if (arr[middle]==x)
        return middle;

        if (arr[middle]>x)
        return binarySearch(arr,l,middle-1,x);
        else
        {
            return binarySearch(arr,middle+1,r,x);
        }
    
    }
    return -1; // element not found
        
    

    
       
 
} 
  
int main(void) 
{ 
    int arr[] = { 2, 3, 4, 10, 40 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    int x = 10; 
    int result = binarySearch(arr, 0, n - 1, x); 
    (result == -1) ? printf("Element is not present in array \n") 
                   : printf("Element is present at index %d \n", 
                            result); 
    return 0; 
} 

/*
// C++ program to implement recursive Binary Search 
#include <bits/stdc++.h> 
using namespace std; 
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{ 
    if (r >= l) { 
        int mid = l + (r - l) / 2; 
  
        // If the element is present at the middle 
        // itself 
        if (arr[mid] == x) 
            return mid; 
  
        // If element is smaller than mid, then 
        // it can only be present in left subarray 
        if (arr[mid] > x) 
            return binarySearch(arr, l, mid - 1, x); 
  
        // Else the element can only be present 
        // in right subarray 
        return binarySearch(arr, mid + 1, r, x); 
    } 
  
    // We reach here when element is not 
    // present in array 
    return -1; 
} 
  
int main(void) 
{ 
    int arr[] = { 2, 3, 4, 10, 40 }; 
    int x = 10; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    int result = binarySearch(arr, 0, n - 1, x); 
    (result == -1) ? cout << "Element is not present in array"
                   : cout << "Element is present at index " << result; 
    return 0; 
} */