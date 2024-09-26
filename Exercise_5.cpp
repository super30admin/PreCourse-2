// Time Complexity: O(n log n) Avg Case, O(n^2) worst case
// Space Complexity: O(log n)
#include <bits/stdc++.h> 
#include<stack>
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
    int pIndex = l;
    int pElement = arr[h];

    for(int i = l; i < h; i++){  // Run the loop from low because each partition side has different low, till high - 1 for partitioning
        if(pElement >= arr[i]){
            swap(&arr[i], &arr[pIndex]);
            pIndex++;
        }
    }
    // swap the pivot element with element at pivot index to complete partitioning
    swap(&arr[pIndex], &arr[h]);
    return pIndex;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    stack<int> s1;
    s1.push(l);
    s1.push(h);

    while(!s1.empty()){
        h = s1.top();
        s1.pop();
        l = s1.top();
        s1.pop();

        int pivotIndex = partition(arr, l,h);

        if(pivotIndex - 1 > l){
            s1.push(l);
            s1.push(pivotIndex - 1);
        }

        if(pivotIndex + 1 < h){
            s1.push(pivotIndex + 1);
            s1.push(h);
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
    int arr[] = { 7, 9, 1, 0, 12, 3, 4, 5, 6, 1, 0, -1, 10 }; 
    int n = sizeof(arr) / sizeof(*arr); 
    quickSortIterative(arr, 0, n - 1); 
    printArr(arr, n); 
    return 0; 
} 