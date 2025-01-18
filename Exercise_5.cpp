/*
Time complexity: O(nlog(n)) - similar to merge sort, logn for division of array and n for partition of sub arrays
Space Complexity: O(log(n)) - due to stack used for partitioning.
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No
*/
#include <iostream> 
#include <stack>
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
    int idx = low-1;
    int pivot = arr[high];

    for (int j = low; j<high;j++) {
        if (arr[j]<=pivot) {
            idx++;
            swap(arr[j], arr[idx]);
        }
    }
    idx++;
    swap(arr[idx], arr[high]);
    return idx;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    stack<pair<int, int>> st;
    st.push({l, h});
    while (!st.empty()) {
        auto curr = st.top();
        st.pop();
        if(curr.first < curr.second){
            int p_ind = partition(arr, curr.first, curr.second);
            if (p_ind-1>curr.first) st.push({curr.first, p_ind-1});
            if (p_ind+1 <curr.second) st.push({p_ind+1, curr.second});
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