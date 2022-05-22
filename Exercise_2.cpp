/*Time complexity = O(n * log(n))
Space complexity = O(n)*/
#include <bits/stdc++.h> 
using namespace std;  
  
// A utility function to swap two elements  
void swap(int* a, int* b)  
{  
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
    int pivot = arr[low];       //Choosing first item for pivot
    int j = low;

    //This loop performs comparisons between the pivot and other elements of the array, and keeps track of j as the pivot position
    for (int i = low + 1; i <= high; i++)
    {   
        if (arr[i] < pivot)
        {
            j++;
            swap(arr[i], arr[j]);
        }
    }
    //item j after the loop is swapped with the actual pivot, and the value of j is returned
    swap(arr[low], arr[j]);

    return j;
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{   
    int pivot;
    if (high > low)
    {
        pivot = partition(arr, low, high);
        quickSort(arr, low, pivot - 1);
        quickSort(arr, pivot + 1, high);
    }

    return; 
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