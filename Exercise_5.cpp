#include <bits/stdc++.h> 
#include <iostream>
#include <stack>
#include <utility>
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
     //Your Code here 
    int i = low, j = low;
    while(j<=high-1){
        if(arr[j]<=arr[high]){
            swap(&arr[i],&arr[j]);
            i++;
        }
        j++;
    }
    swap(&arr[i],&arr[high]);
    return i;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    stack<pair<int,int> >params;
    pair<int,int>curr;
    curr.first = l;
    curr.second = h;
    params.push(curr);
    while(!params.empty()){
        pair<int,int>curr = params.top();
        params.pop();
        int low = curr.first, high = curr.second;
        if(low>=high) continue;
        int low_part = partition(arr,low,high);
        pair<int,int>left_curr;
        left_curr.first = low;
        left_curr.second = low_part-1;
        pair<int,int> right_curr;
        right_curr.first = low_part+1;
        right_curr.second = high;
        params.push(left_curr);
        params.push(right_curr);
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