/**
 * Time Complexity:
 * The time complexity O(n^2) in worst case
 */

/**
 * Space Complexity:
 * For worst case the space complexity is O(n)
 * 
 */

/**
 * Approach:
 * There are many quick sort algorithms based on the decision of position of pivot.
 * Here we have assumed our pivot to be the last element. Based on this pivot we do
 * comparisons and put all the elements which are smaller than the pivot element
 * before the pivot element and rest of the elements are put after it.
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
int partition(int arr[], int l, int h) 
{ 
    //Do the comparison and swapping here 
    int temp = arr[h];
    int idxSmaller = l-1;
    for (int j = l; j < h; j++) {
        if (arr[j] <= temp) {
            idxSmaller++;
            swap(&arr[idxSmaller], &arr[j]);
        }
    }
    swap(&arr[idxSmaller + 1], &arr[h]);
    return (idxSmaller + 1);
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 

    int stack[h - l + 1];
    int top = -1;
    stack[++top] = l;
    stack[++top] = h;
    while (top >= 0) {
        h = stack[top--];
        l = stack[top--];
        int p = partition(arr, l, h);
        if (p - 1 > l) {
            stack[++top] = l;
            stack[++top] = p - 1;
        }
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