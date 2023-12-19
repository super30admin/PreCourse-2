// Time Complexity :
// Space Complexity :
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : not getting the intuition how the stack will be used to avoid recursion
#include <bits/stdc++.h> 
#include <stack>
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
     int pivotVal = arr[h];
    int i = l - 1;
    int j = l;
    int k = h + 1;
    while (j < k)
    {
        if (arr[j] < pivotVal)
        {
            swap(arr[i + 1], arr[j]);
            i++;
            j++;
        }
        else if (arr[j] > pivotVal)
        {
            swap(arr[j], arr[k - 1]);
            k--;
        }
        else
        {
            j++;
        }
    }
    return i + 1;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    if (l < h)
    {
        stack<int> st;
        st.push(l);
        st.push(h);
        while(!st.empty())
        {
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