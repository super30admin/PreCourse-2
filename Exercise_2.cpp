#include <bits/stdc++.h> 
using namespace std;  
  
// A utility function to swap two elements  
void swap(int* a, int* b)  
{  
    //Your Code here 
    int temp = *a;
    *a = *b;
    *b = temp;
}  


/* This function takes last element as pivot, places  
the pivot element at its correct position in sorted  
array, and places all smaller (smaller than pivot)  
to left of pivot and all greater elements to right  
of pivot */

/* Find element smaller than pivot from right side.  
*  Find element larger than pivot from left side.
*  Swap elements if index of smaller element is less than index of larger element, else
*  swap the pivot element with the larger element and return the larger element location for partition. 
*  Call quicksort algo on both partitions, (low, part-1) and (part + 1, high) 
*/

// Best and Average case time Complexity : O(nlog n)
// Worst case time complexity : O(n^2)
// Worst case space Complexity : O(n)
// Best and Average case space Complexity : O(log n)

int partition (int arr[], int low, int high)  
{  
    //Your Code here 
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
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
    //Your Code here
    if (low >= high)
        return;

    int part = partition(arr, low, high);
    quickSort(arr, low, part - 1);
    quickSort(arr, part + 1, high);
}  
  
/* Function to print an array */
void printArray(int arr[], int size)  
{  
    int i;  
    for (i = 0; i < size; i++)  
        cout << arr[i] << " ";  
    cout << endl;  
}  
  
// Driver Code 
int main()  
{  
    int arr[] = {10, 7, 8, 9, 1, 5};  
    int n = sizeof(arr) / sizeof(arr[0]);  
    quickSort(arr, 0, n - 1);  
    cout << "Sorted array: \n";  
    printArray(arr, n);  
    return 0;  
}  