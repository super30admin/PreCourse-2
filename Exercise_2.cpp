/*
Time complexity: O(nlog(n)) - similar to merge sort, logn for division of array and n for partition of sub arrays
Space Complexity: O(1) - no extra space if recursion stack space is ignored. 
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No
*/
#include <iostream> 
using namespace std;  
    
/* This function takes last element as pivot, places  
the pivot element at its correct position in sorted  
array, and places all smaller (smaller than pivot)  
to left of pivot and all greater elements to right  
of pivot */
int partition (int arr[], int low, int high)  
{  
    //Your Code here 
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
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
    if (low < high) {
        int p_ind = partition(arr, low, high);
        quickSort(arr, low, p_ind-1);
        quickSort(arr, p_ind+1, high);
    }
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