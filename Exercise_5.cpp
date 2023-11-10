// Time Complexity :O(n^2)
// Space Complexity :O(logn)

#include <bits/stdc++.h> 
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
int partition(int arr[], int l, int h) 
{ 
    //Do the comparison and swapping here 
      int pivot=arr[h];
    int partitionIndex=l;
    for(int i=l;i<h;i++)
    {
        if(arr[i]<=pivot)
        {
            swap(arr[i],arr[partitionIndex]);
            partitionIndex++; 
        }
    }
    swap(arr[partitionIndex],arr[h]);
    return partitionIndex;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    stack<pair<int,int>> st1;
    st1.push(make_pair(l,h));

    while(!st1.empty())
    {
        l=st1.top().first;
        h=st1.top().second;
        st1.pop();

        int pivot=partition(arr,l,h);
        if(pivot-1>l)
        {
            st1.push(make_pair(l,pivot-1));

        }
        if(pivot+1<h)
        {
            st1.push(make_pair(pivot+1,h));
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
