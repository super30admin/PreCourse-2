#include <bits/stdc++.h> 
using namespace std; 
  
// A utility function to swap two elements 
void swap(int* a, int* b) 
{ 
    int t = *a; 
    *a = *b; 
    *b = t; 
} 

/* Push start and end index pair on stack. 
*  Repeat the following steps until stack is empty.
*  Pop element from stack. Assign first value to low and second value to high.
*  Find element smaller than pivot from right side.  
*  Find element larger than pivot from left side.
*  Swap elements if index of smaller element is less than index of larger element, else
*  swap the pivot element with the larger element and return the larger element location for partition. 
*  Push (low, part-1) and (part + 1, high) on stack. 
*/

// Best and Average case time Complexity : O(nlog n)
// Worst case time complexity : O(n^2)
// Worst case space Complexity : O(n)
// Best and Average case space Complexity : O(log n)

/* This function is same in both iterative and recursive*/
int partition(int arr[], int low, int high) 
{ 
    //Do the comparison and swapping here 

    int pivot = arr[high];
    int small, big, l, h;

    l = low;
    h = high - 1;

    while (l < h)
    {
        while (h > 0 && arr[h] > pivot)
            h--;

        while (l < high  && arr[l] <= pivot)
            l++;

        if (l < h)
            swap(arr[l], arr[h]);
    }

    swap(arr[l], arr[high]);
    return l;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    //Your Code here

    int low, high;

    stack<pair<int, int>> st;
    st.push({l, h});

    while (!st.empty())
    {
        /* code */
        auto element = st.top();
        low = element.first;
        high = element.second;
        st.pop();

        if (low >= high)
            continue;

        int part = partition(arr, low, high);
        
        st.push({low, part - 1});
        st.push({part + 1, high});
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