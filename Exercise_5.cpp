#include <bits/stdc++.h> 
using namespace std; 
  
// A utility function to swap two elements 
void swap(int* a, int* b) 
{ 
    int t = *a; 
    *a = *b; 
    *b = t; 
} 
  
/* This function is same in both iterative and recursive */

// Time Complexity: O(n)
// Space Complexity: O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

int partition(int arr[], int l, int h) 
{ 
    int pivot = arr[h];  // Select the rightmost element as the pivot
    int i = l - 1;  // Index of the smaller element

    for (int j = l; j < h; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[h]);
    return (i + 1);
} 
  
/* A[] --> Array to be sorted,  
   l --> Starting index,  
   h --> Ending index */

// Time Complexity: O(n^2)
// Space Complexity: O(logn)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

void quickSortIterative(int arr[], int l, int h) 
{ 
    // Create an auxiliary stack
    int stack[h - l + 1];

    // Initialize top of the stack
    int top = -1;

    // Push initial values of l and h to the stack
    stack[++top] = l;
    stack[++top] = h;

    // Keep popping from the stack while it is not empty
    while (top >= 0) {
        // Pop h and l
        h = stack[top--];
        l = stack[top--];

        // Set pivot element at its correct position in sorted array
        int p = partition(arr, l, h);

        // If there are elements on the left side of the pivot, push them to the stack
        if (p - 1 > l) {
            stack[++top] = l;
            stack[++top] = p - 1;
        }

        // If there are elements on the right side of the pivot, push them to the stack
        if (p + 1 < h) {
            stack[++top] = p + 1;
            stack[++top] = h;
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
