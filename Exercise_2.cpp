/**
 * Time Complexity:
 * The time complexity O(n^2) in worst case
 */

/**
 * Space Complexity:
 * For worst case the space complexity is O(n)
 * 
 */

/**
 * Approach:
 * There are many quick sort algorithms based on the decision of position of pivot.
 * Here we have assumed our pivot to be the last element. Based on this pivot we do
 * comparisons and put all the elements which are smaller than the pivot element
 * before the pivot element and rest of the elements are put after it.
 */

// The code ran perfectly


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
int partition (int arr[], int low, int high)  
{  
    //Your Code here 
    int pivot = arr[high];
    int idxSmaller = (low - 1);
    for (int i = low; i < high; i++)
    {
        if(pivot > arr[i] ){
            idxSmaller++;
            swap(&arr[idxSmaller], &arr[i]);
        }
    }
    swap(&arr[idxSmaller+1], &arr[high]);
    return (idxSmaller+1);
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
    //Your Code here 
     if (low < high)
    {
        
        int idxPart = partition(arr, low, high);
 
    
        quickSort(arr, low, idxPart - 1);
        quickSort(arr, idxPart + 1, high);
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