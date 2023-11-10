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
    int j = l;
    for(int i = l; i < h; i++) {
        if(arr[i] <= pivot)
            swap(arr[i], arr[j++]);
    }
    swap(arr[h], arr[j]);
    return j; 
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 

    stack<pair<int, int>> st;
    st.push(make_pair(l, h));
    while(!st.empty()) {
        l = st.top().first;
        h = st.top().second;
        st.pop();

        int pivot = partition(arr, l, h);
        if(pivot - 1 > l) st.push(make_pair(l, pivot - 1));
        if(pivot + 1 < h) st.push(make_pair(pivot + 1, h));
    }} 
  
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