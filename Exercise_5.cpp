/*
TC: Same as the recursive version, O(nlogn) for best/average case and O(n^2) for worst case.
SC: This approach requires O(logn) space in the best/average case and O(n) in the worst case. 
Explanation in Sample.java 
*/ 

#include <bits/stdc++.h> 
using namespace std; 
  
// A utility function to swap two elements 
void swap(int* a, int* b) 
{ 
    if(*a == *b) return;
    *a = *a + *b;
    *b = *a - *b;
    *a = *a - *b;
} 
  
/* This function is same in both iterative and recursive*/
int partition(int arr[], int low, int high) 
{ 
    //Do the comparison and swapping here 
    int pivot = arr[high];
    int i = low; // iterator for the left partition
    int j = high; // iterator for the right partition
    while(i < j){ // to ensure that the left & right iterators don't cross each other 
        while(i<=high && arr[i] < pivot){ // fi nd first element in the left partition which does not satisfy our constraints
            i++;
        }
        while(j>=low && arr[j] >= pivot) { // find first element in the right partition which does not satisfy our constraints
            j--;
        }
        if(i < j){ // to make sure that the swap is still valid (we don't want to accidentally swap elements which are in the correct partition)
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i], &arr[high]); // the index where the left iterator spills into the right partition will be the correct position of the pivot
    return i; // return index of pivot
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    stack<pair<int, int>> ranges;
    ranges.push({l,h});
    while(!ranges.empty()) {
        pair<int, int> top = ranges.top();
        ranges.pop();
        int low = top.first; // destructuring pair into low and high for better variable names & readability
        int high = top.second; 
        if(low < high) {
            int pIndex = partition(arr, low, high);
            ranges.push({low, pIndex - 1});
            ranges.push({pIndex + 1, high});
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

bool isSorted(int A[], int size) {
    for(int i=1; i<size; i++){
        if(A[i-1] > A[i]) return false;
    }
    return true;
}
  
// Driver code 
int main() 
{ 
    /* TEST CASES */
    int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
    // int arr[] = {}; // empty array
    // int arr[] = {1}; // array with only one element (already sorted)
    // int arr[] = {1, 2, 3, 4}; // already sorted array
    // int arr[] = {1, 3, 2, 1, 2, 3, 4, 1, 4, 2, 3}; // array with duplicates
    // int arr[] = {5,-1,3,0,-2,4,-3}; // negatives
    // int arr[] = {INT_MIN, 0, INT_MIN, INT_MAX}; // extreme values
    int n = sizeof(arr) / sizeof(*arr); 

    if(n == 0) {
        cerr<<"Invalid array"<<endl;
        return 1;
    } 

    if(n == 1 || isSorted(arr, n)){
        cout<<"Array is already sorted."<<endl;
        return 0;
    } 

    quickSortIterative(arr, 0, n - 1); 
    printArr(arr, n); 
    return 0; 
} 