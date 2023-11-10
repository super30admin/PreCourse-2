// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Any problem you faced while coding this : Was unable to solve this, had to look for help online and understand how to implement.


#include <bits/stdc++.h> 
using namespace std; 
  
// A utility function to swap two elements 
void swap(int* a, int* b) 
{ 
    int t = *a; 
    *a = *b; 
    *b = t; 
} 
  
/* This function is same in both iterative and recursive*/
int partition(int arr[], int l, int h) 
{ 
    //Do the comparison and swapping here
    int pivot = arr[h];
    int pIndex = 0;
    for(int i=0; i<h; ++i)
    {
        if(arr[i] <=pivot)
        {
            swap(arr[i], arr[pIndex]);
            pIndex++;
        }
    } 
    swap(arr[h], arr[pIndex]);
    return pIndex;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    stack<pair<int, int>> s;
 
    // push the start and end index of the array into the stack
    s.push(make_pair(l, h));
 
    // loop till stack is empty
    while (!s.empty())
    {
        // remove top pair from the list and get subarray starting
        // and ending indices
        l = s.top().first, h = s.top().second;
        s.pop();
 
        // rearrange elements across pivot
        int pivot = partition(arr, l, h);
 
        // push subarray indices containing elements that are
        // less than the current pivot to stack
        if (pivot - 1 > l) {
            s.push(make_pair(l, pivot - 1));
        }
 
        // push subarray indices containing elements that are
        // more than the current pivot to stack
        if (pivot + 1 < h) {
            s.push(make_pair(pivot + 1, h));
        }
    }
} 
  
// A utility function to print contents of arr 
void printArr(int arr[], int n) 
{ 
    int i; 
    for (i = 0; i < n; ++i) 
        cout << arr[i] << " "; 
} 
  
// Driver code 
int main() 
{ 
    int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
    int n = sizeof(arr) / sizeof(*arr); 
    quickSortIterative(arr, 0, n - 1); 
    printArr(arr, n); 
    return 0; 
} 