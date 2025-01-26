// Time Complexity : O(n log n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : -
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach
//stack stores the indices of the lower and upper boundaries.
//After finding the partition index, if there exist a left/right arrays then it's indices are stored.
//each boundary in the stack is handled iteratively and sorted


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
    int pivot = arr[high];
    int small = low-1;
    for(int i=low; i<high; i++){
        if(arr[i] <= pivot){
            small++;
            swap(&arr[small], &arr[i]);
        }
    }
    swap(&arr[small+1], &arr[high]);
    return (small+1);
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    stack<pair<int,int>> st;
    st.push({l,h});
    while(!st.empty()){
        pair<int,int> p = st.top();
        st.pop();
        int low = p.first;
        int high = p.second;
        int pIdx = partition(arr,low,high);

        if(pIdx-1 > low){
            st.push({low,pIdx-1});
        }
        if(pIdx+1 < high){
            st.push({pIdx+1,high});
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