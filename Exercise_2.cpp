#include <bits/stdc++.h> 
using namespace std;  
  
// A utility function to swap two elements  
void swap(int* a, int* b)  
{  
    int t = *a; 
    *a = *b; 
    *b = t; 

    return;
}  
  
/* This function takes last element as pivot, places  
the pivot element at its correct position in sorted  
array, and places all smaller (smaller than pivot)  
to left of pivot and all greater elements to right  
of pivot */
int partition (int arr[], int low, int high)  
{  
    int p = arr[low];

    int i = low;
    int j = high;

    //Loop to keep swapping elements
    while(i < j)
    {
        //Find the next higher number
        while(arr[i] <= p)
        {
            i++;
        }

        //Find the next lower number
        while(arr[j] > p)
        {
            j--;
        }

        if(i < j)
        {
            swap(&arr[i], &arr[j]);
        }
    }

    //Shift Pivot to correct location
    swap(&arr[low], &arr[j]);

    return j;
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
    int j;

    if(low < high)
    {
        //Find a Pivot element index present
        // at it's correct position
        j = partition(arr, low, high);

        //Quick sort the left and right halves
        quickSort(arr, low, j);
        quickSort(arr, j+1, high);       
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

/**
 * @brief COmplexity Analysis
 * Time - Average Case O(nlogn), Worst Case - O(n*n)
 * Space - In-place
 */