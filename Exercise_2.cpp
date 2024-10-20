#include <bits/stdc++.h> 
using namespace std;  
  
// A utility function to swap two elements  
void swap(int* a, int* b)  
{  
    //Your Code here 
    int temp = *a; 
     *a=*b;
     *b = temp;
}  
  
/* This function takes last element as pivot, places  
the pivot element at its correct position in sorted  
array, and places all smaller (smaller than pivot)  
to left of pivot and all greater elements to right  
of pivot */
int partition (int arr[], int low, int high)  
{  
    int piviot = arr[high];
    int i = low;
    int j = high-1;
    while(i<j){
        while(arr[i]<=piviot && i<high){
            i++;
        }
        while(arr[j]>=piviot && j>low){
            j--;
        }
        if(i<j){
            swap(arr[i],arr[j]);
            }
    }
    swap(arr[high],arr[i]);
    return i;
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
    //Your Code here
    if(low<high){
        int ind = partition(arr,low, high);
        quickSort(arr,low, ind-1);            //left sort
        quickSort(arr,ind+1, high);           //right sort
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