// Time Complexity : O(nlog n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode :yes
// Any problem you faced while coding this :none


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
    int pivot = arr[high];
    int i=low;
    for(int j=low; j<high; j++){
        if(arr[j] < arr[high]){
            swap(&arr[i],&arr[j]);
            i++;
        }
    }
    swap(&arr[i],&arr[high]);
    return i;
    
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    stack<int> stk;
    stk.push(l);
    stk.push(h);
    
    while(!stk.empty()) {
        int h = stk.top();
        stk.pop();
        int l = stk.top();
        stk.pop();
        int pi = partition(arr, l, h);
        if(l<pi-1){
          stk.push(l);
          stk.push(pi-1);
        }
        if(pi+1 < h){
          stk.push(pi+1);
          stk.push(h);
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
    int arr[] = { 4, 3,9,9,8, 5, 2, 1, 10,6, 7, 4, 3, 2, 3 }; 
    int n = sizeof(arr) / sizeof(*arr); 
    quickSortIterative(arr, 0, n - 1); 
    printArr(arr, n); 
    return 0; 
} 



