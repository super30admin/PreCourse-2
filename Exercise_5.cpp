/*
----------------------------------------
* Implemetation of Itereative Quick Sort
----------------------------------------

* Time Complexity:
*        - Average Case: O(nlog(n))
*        - Worst Case: O(n^2)

* Space Complexity:
*        - Average Case: O(log(n))
*        - Worst Case: O(n)

Did this code successfully run on Leetcode : NA
Any problem you faced while coding this : NO

*/

#include <bits/stdc++.h>
#include <utility>
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
    int pivot = arr[h]; // pivot at end is chosen
    int pivot_index = l;

    for (int i = l; i < h; i++) {
        if (arr[i] <= pivot) {
            swap(arr[i], arr[pivot_index]);
            pivot_index++;
        }
    }

    swap(arr[pivot_index], arr[h]);
    return pivot_index;
}

/* A[] --> Array to be sorted,
l --> Starting index,
h --> Ending index */
void quickSortIterative(int arr[], int l, int h)
{
    //Try to think that how you can use stack here to remove recursion.
    int stack[h - l + 1];

    int top = -1;

    // pushing the initial values of l and h to stack
    stack[++top] = l;
    stack[++top] = h;

    while (top >= 0) {
        h = stack[top--];
        l = stack[top--];

        int p = partition(arr, l, h);
        // If there are elements on left side of pivot, then push left side to stack
        if (p - 1 > l) {
            stack[++top] = l;
            stack[++top] = p - 1;
        }

        // If there are elements on right side of pivot, then push right side to stack
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
    cout << endl;
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