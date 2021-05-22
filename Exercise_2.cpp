#include <bits/stdc++.h> 
using namespace std;  
  
// A utility function to swap two elements  
void swap(int a[], int i, int j)  
{  
    //Your Code here 
    int t;
    t = a[i];
    a[i] = a[j];
    a[j] = t;
}  
  
/* This function takes last element as pivot, places  
the pivot element at its correct position in sorted  
array, and places all smaller (smaller than pivot)  
to left of pivot and all greater elements to right  
of pivot */
int partition (int a[], int low, int high)  
{  
    //Your Code here 
    int i, j, piv, temp;
    piv = a[high];
    i = low - 1;
    for(j = low; j <= high - 1; j++) {
        if(a[j] < piv) {
            i++;
            swap(a, i, j);
        }
    }
    swap(a, i + 1, high);
    return (i + 1);
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int a[], int low, int high)  
{  
    //Your Code here 
    if(low < high) {
        int piv = partition(a, low, high);
        quickSort(a, low, piv - 1);
        quickSort(a, piv + 1, high);
    }    
}  
  
/* Function to print an array */
void printArray(int a[], int size)  
{  
    int i;  
    for (i = 0; i < size; i++)  
        cout << a[i] << " ";  
    cout << endl;  
}  
  
// Driver Code 
int main()  
{  
    int a[] = {10, 7, 8, 9, 1, 5};  
    int n = sizeof(a) / sizeof(a[0]);  
    quickSort(a, 0, n - 1);
    cout << "Sorted array: \n";  
    printArray(a, n);  
    return 0;  
}  