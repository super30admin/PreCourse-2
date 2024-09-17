#include <bits/stdc++.h> 
using namespace std; 

/*
Time Complexity - worst case O(N^2)
Time Complexity - average case O(NlogN)
Space complexity - O(N)
*/
  
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
    int idx = l - 1; //index of last smallest element than pivot
    for (int i = l; i < h; ++i){
        if (arr[i] <= pivot){
            swap(&arr[i], &arr[++idx]);
        }
    }
    swap(&arr[h], &arr[idx + 1]);
    return idx + 1;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    stack<int> s;
    // push low and high indices to stack
    s.push(l); s.push(h);
    while (!s.empty()){
        int right = s.top(); s.pop();
        int left = s.top(); s.pop();
        int pi = partition(arr, left, right);
        // check if there are elements present to left of pivot
        if (pi - 1 >= left){
            s.push(left); s.push(pi - 1);
        }
        //check if there are elements present to right of pivot
        if (pi + 1 <= right){
            s.push(pi + 1); s.push(right);
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
    int arr[] = { 4, 3 }; 
    int n = sizeof(arr) / sizeof(*arr); 
    quickSortIterative(arr, 0, n - 1); 
    printArr(arr, n); 
    return 0; 
} 
