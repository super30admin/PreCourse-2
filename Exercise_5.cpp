#include<iostream>
#include<stack>
using namespace std; 

// Time Complexity : O(n log n) 
// Space Complexity : O(n) //Extra space for stack
// Any problem you faced while coding this : No

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
    int temp_l = l;
    for(int i = l; i < h; i++)
    {
        if(arr[i] < pivot)
        {
            swap(&arr[i],&arr[temp_l]);
            temp_l++;
        }
    }

    swap(&arr[temp_l], &arr[h]);

    return temp_l;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    stack<int> s;
    s.push(l);
    s.push(h);

    while(!s.empty())
    {
        h = s.top();
        s.pop();
        l = s.top();
        s.pop();

        int pivot_index = partition(arr, l , h);

        //Left subarray if any
        if(pivot_index - 1 > l)
        {
            s.push(l);
            s.push(pivot_index - 1);
        }

        //Right subarray if any
        if(pivot_index + 1 < h)
        {
            s.push(pivot_index + 1);
            s.push(h);
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