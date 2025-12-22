//Time Complexity : O(n logn)
// Space Complexity : O(logn)

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
    int pivot = arr[h];
    int i = l - 1;

    for (int j = l; j <= h - 1; j++)
    {
        if (arr[j] <= pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[h]);
    return i + 1;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    // Create an explicit stack
    stack<int> st;

    // Push initial values
    st.push(l);
    st.push(h);

    // Pop until stack is empty
    while (!st.empty())
    {
        h = st.top(); st.pop();
        l = st.top(); st.pop();

        int p = partition(arr, l, h);

        // If elements on left side of pivot
        if (p - 1 > l)
        {
            st.push(l);
            st.push(p - 1);
        }

        // If elements on right side of pivot
        if (p + 1 < h)
        {
            st.push(p + 1);
            st.push(h);
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