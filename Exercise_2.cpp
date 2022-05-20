
// Time Complexity : Average case O( n log(n) ) as each time the array gets divided into two parts ( log n ) and iteration of array cause the n times for each.
                     // worst case can be O( n*n ) but randomized pivot element can help in dividing the array into two almost equal halves. 
// Space Complexity : No extra space complexity. In place swapping.
// Any problem you faced while coding this : 
// only partially remembered the algo, but after revising was able to write.

// Your code here along with comments explaining your approach
/* Divide and conquer approach on array and on each iteraion making the pivot element in correct position. */

#include<iostream>
using namespace std;  
  
// A utility function to swap two elements  
void swap(int* a, int* b)  
{  
    //Your Code here
    int temp = *b;
    *b = *a;
    *a = temp;
}  
  
/* This function takes last element as pivot, places  
the pivot element at its correct position in sorted  
array, and places all smaller (smaller than pivot)  
to left of pivot and all greater elements to right  
of pivot */
int partition (int arr[], int low, int high)  
{  
    //Your Code here 
    int index = low;
    int pivot = high;
    int temp = low;
    // going till just before the pivot element hence < not <=
    while( temp < high ) {
        if ( arr[temp] <= arr[pivot] ){
           swap( &arr[temp], &arr[index] );
	   index = index + 1;
        }
        temp = temp + 1;
    }
    // swapping the pivot with index so pivot is at correct position.
    swap( &arr[pivot], &arr[index] );
    return index;
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
    //Your Code here
    if( low >= high ) {
        // >= because with one element it is already sorted
        return; 
    }
    int index = partition( arr, low, high );
    quickSort( arr, low, index - 1 );
    quickSort( arr, index+1 , high );
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
