/*

TC: O(n2) worst case, O(nlgn) avg case
SC: O(1)
Logic:
We are just mimicing a recursion by using a real one. We are passing the exact same parameters we passed to recursive function and pushing into the stack in the exact same order, this results in 
the exact same behaviour as a recursion stack.

*/
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
int partition(int arr[], int low, int high) 
{ 
    int pivot = arr[high];
    int i = low-1;
    for(int j=low; j<high; j++)    
        if(arr[j] < pivot)  i++, swap(&arr[i], &arr[j]);
    swap(&arr[i+1], &arr[high]);
    return i+1;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    stack<pair<int, int>> quickSortStack;
    quickSortStack.push(make_pair(l, h));
    while(!quickSortStack.empty())  {
        auto cur = quickSortStack.top();    quickSortStack.pop();
        int low = cur.first, high=cur.second; 
        if(low > high)  continue;
        int pi = partition(arr, low, high);
        quickSortStack.push(make_pair(low, pi-1));
        quickSortStack.push(make_pair(pi+1, high));
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