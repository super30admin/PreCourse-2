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
// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : No

int partition (int arr[], int l, int h)
{
    int pivot = arr[h];
    int index = (l - 1);  
 
    for (int i = l; i <= h- 1; i++)
    {
        // If current element is smaller than or equal to pivot, swap
        if (arr[i] <= pivot)
        {
            index++;
            swap(&arr[index], &arr[i]);
        }
    }
    swap(&arr[index + 1], &arr[h]);
    return (index + 1);
}
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : No

void quickSortIterative(int arr[], int l, int h) 
{ 
    // Creating a stack using array same len as arr
    int stack[h - l + 1];
 
    // init top variable
    int top = -1;
    top += 1;
    stack[top] = l;
    top += 1;
    stack[top] = h;
 
    // Keep popping from stack while is not empty
    while (top >= 0) {
        h = stack[top];
        top -= 1;
        l = stack[top];
        top -= 1;
 
        // Placing the pivot in its index
        int p = partition(arr, l, h);
 
        // push left side to stack if less side of arr exists
        if (p - 1 > l) {
            top += 1;
            stack[top] = l;
            top += 1;
            stack[top] = p - 1;
        }
 
        // push right side to stack if right side of arr exists
        if (p + 1 < h) {
            top += 1;
            stack[top] = p + 1;
            top += 1;
            stack[top] = h;
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