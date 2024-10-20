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
    //Do the comparison and swapping here 
    //same as ex2
    int piviot = arr[high];
    int i = low;
    int j = high;
    while(i<j){
        while(arr[i]<=piviot && i<high){
            i++;
        }
        while(arr[j]>=piviot && j>low){
            j--;
        }
        if(i<j){
            swap(arr[i],arr[j]);
            }
    }
    swap(arr[high],arr[i]);
    return i;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    int n = h-l+1;
    int stack[n];
    int top = -1;
    stack[++top] = l; 
    stack[++top] = h;
    while (top >= 0) 
    { 
        h = stack[top--]; 
        l = stack[top--]; 
        int p = partition(arr, l, h); 
        if (p - 1 > l) 
        { 
            stack[++top] = l; 
            stack[++top] = p - 1; 
        } 
        if (p + 1 < h) 
        { 
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