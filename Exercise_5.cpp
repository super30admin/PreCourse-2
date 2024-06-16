/*
 *                     Iterative way of using Quick sort algorithm 
 *
 * Time Complexity  : O(nlogn) and O(n^2)-->Worst case 
 * Space Complexity : O(logn)  and O(n)--> Worse Case
 * Did this code successfully run on Leetcode/VSCode : Yes
 * Any problem you faced while coding this : No
 * Your code here along with comments explaining your approach :
 *          Using stacks to manage sub-array boundaries
 *          Using pivot to partition into sub-arrays 
 *          By pushing and popping indices into stack, iteratively sorting the entire array.
 */

#include <iostream>
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
    //Do the comparison and swapping here
    int pivot = arr[h];
    int pIndex = l;
       for(int i = l; i < h; i++) {
        if (arr[i] <= pivot) {
            swap(&arr[i], &arr[pIndex]);
            pIndex++;
        }
    }
    swap(&arr[pIndex], &arr[h]);
    return pIndex;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
// Iterative Quick Sort function
void quickSortIterative(int arr[], int low, int high) {
    // Create an auxiliary stack
    stack<int> stk;

    // Push initial values of low and high to stack
    stk.push(low);
    stk.push(high);

    // Keep popping from stack while it is not empty
    while (!stk.empty()) {
        // Pop high and low
        high = stk.top();
        stk.pop();
        low = stk.top();
        stk.pop();

        // Set pivot element at its correct position
        int p = partition(arr, low, high);

        // If there are elements on the left side of the pivot,
        // push left side to stack
        if (p - 1 > low) {
            stk.push(low);
            stk.push(p - 1);
        }

        // If there are elements on the right side of the pivot,
        // push right side to stack
        if (p + 1 < high) {
            stk.push(p + 1);
            stk.push(high);
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
