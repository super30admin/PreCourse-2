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
    int pivot = h;
    int i = (l - 1), j;

    for (j = l; j < h; j++) {
        if (arr[j] < arr[pivot]) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[pivot]);
    return i + 1;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{
    int start, end;
    stack<int> s;
    
    s.push(l);
    s.push(h);

    while (!s.empty()) {
        end = s.top();
        s.pop();
        start = s.top();
        s.pop();

        int pivot = partition(arr, start, end);

        if ((pivot - 1) > start) {
            s.push(start);
            s.push(pivot - 1);
        }

        if ((pivot + 1) < end) {
            s.push(pivot + 1);
            s.push(end);
        }
    }
} 
  
// A utility function to print contents of arr 
void printArr(int arr[], int n) 
{ 
    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " "; 
    }

    cout << endl;
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
