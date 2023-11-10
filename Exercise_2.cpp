#include <bits/stdc++.h> 
using namespace std;  
  
// A utility function to swap two elements  
void swap(int* a, int* b)  
{  
      int t = *a;
  *a = *b;
  *b = t;
}  
  
/* This function takes last element as pivot, places  
the pivot element at its correct position in sorted  
array, and places all smaller (smaller than pivot)  
to left of pivot and all greater elements to right  
of pivot */
int partition (int arr[], int low, int high)  
{  
     int i=low,j=high;
    int pivot = arr[low];
  while(i<j){
    do{
      i++;
    }while(arr[i] <= pivot);
    do{
      j--;
    }while(arr[i] > pivot);
    if(i<j){
        swap(arr[i],arr[j]);
    }
  }
  swap(arr[low],arr[j]);
  return j;
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
       if(low<high){
      int j= partition(arr,low,high);
      quickSort(arr,low,j);
      quickSort(arr,j+1,high);
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