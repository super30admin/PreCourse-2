// Time Complexity : worst case: n^2 avg and best case: O(n log n)
// Space Complexity : worst case: O(n) and best case: O(n log n)
// Did this code successfully run on Leetcode : no. will work on it
// Any problem you faced while coding this : learnt it today


// Your code here along with comments explaining your approach
#include <bits/stdc++.h> 
using namespace std;  
  
// A utility function to swap two elements  
void swap(int* a, int* b)  //This function is used when to swap the 'left' elements with 'right' elements wrt pivot
{  
    //Your Code here 
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
    //Your Code here 
    int pivot = arr[high], temp;
    int l = low, r = high;
    
    while(l<r){
        while(arr[l]<pivot){    //keep incrementing l until a value that needs to be moved to right is found.
            l++;
        }
        while(arr[r]>=pivot){   //keep decrementing r until a value that needs to be moved to left is found.
            r--;
        }
        if(l<r){
            swap(&arr[l], &arr[r]);  //if there exists some elements that need to be moved, call the swap function
        }
    }
    arr[high] = arr[l];  //when l>r, the new high is arr[l]
    arr[l] = pivot;     //new pivot is new last number
    
    return l;  //returns the pivot index
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
    //Your Code here 
    if(low<high){                                        
        int partition_index = partition(arr, low, high);  //find pivot as its the sorted element
        quickSort(arr, low, partition_index-1);           //sort left half(by finding pivot and sorting its left half and so on)
        quickSort(arr, partition_index+1, high);          //sort right half(by finding pivot and sorting its right half and so on)
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