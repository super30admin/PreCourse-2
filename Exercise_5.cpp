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
    int i = l - 1; // index of smaller element

    for (int j = l; j <= h - 1; j++) {
        if (arr[j] < pivot) {
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
void quickSortIterative(int arr[], int l, int h) 
{ 
    // Create auxiliary stack
    stack<int> s;

    // Push initial values
    s.push(l);
    s.push(h);

    // Keep popping until stack is empty
    while (!s.empty()) {
        // Pop h and l
        h = s.top();
        s.pop();
        l = s.top();
        s.pop();

        // Partition the array
        int p = partition(arr, l, h);

        // If elements on the left of pivot, push left subarray
        if (p - 1 > l) {
            s.push(l);
            s.push(p - 1);
        }

        // If elements on the right of pivot, push right subarray
        if (p + 1 < h) {
            s.push(p + 1);
            s.push(h);
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
