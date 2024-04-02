// Time Complexity : worst is O(n2) and avg O(nlog n)
// Space Complexity : o(1)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :

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
  
/* This function:
a) takes last element as pivot, 
b) places the pivot element at its correct position in sorted  
   array, 
c) places all smaller than pivot elements to left of pivot 
d) places all greater than pivot elements to right of pivot 
*/
int partition (int arr[], int low, int high)  
{  
    int pivot = arr[high];
    int i=low;
    for(int j=low; j<high; j++){
        if(arr[j] < arr[high]){
            swap(&arr[i],&arr[j]);
            i++;
        }
    }
    swap(&arr[i],&arr[high]);
    return i;
    
    
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
    if(low < high) {
       int pi = partition(arr,low,high);
       quickSort(arr, low, pi-1); 
       quickSort(arr, pi+1, high); 
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
    
    int arr1[] = {10, 2, 4, 10, 9 , 7, 8, 9, 1, 5};  
    n = sizeof(arr1) / sizeof(arr1[0]);  
    quickSort(arr1, 0, n - 1);  
    cout << "Sorted array: \n";  
    printArray(arr1, n);  
    return 0;  
}  
