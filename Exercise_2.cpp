#include <bits/stdc++.h> 
using namespace std;  
  
// A utility function to swap two elements  
void swap(int* a, int* b)  
{  
    int temp;
    temp = *a;
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
    int pIndex = low;
    int pElement = arr[high];

    for(int i = low; i < high; i++){  // Run the loop from low because each partition side has different low, till high - 1 for partitioning
        if(pElement >= arr[i]){
            swap(&arr[i], &arr[pIndex]);
            pIndex++;
        }
    }
    // swap the pivot element with element at pivot index to complete partitioning
    swap(&arr[pIndex], &arr[high]);
    return pIndex; 
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
    if(low < high){
        int pivotIndex = partition(arr, low, high);     // Took pivotIndex to avoid confusion with pIndex of Partition function
        quickSort(arr, low, pivotIndex - 1);    // The left partition
        quickSort(arr, pivotIndex + 1, high);   // The right partition
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