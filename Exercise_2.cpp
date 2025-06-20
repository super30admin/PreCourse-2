// Time Complexity :O(nlogn)- average, best and O(n^2) - worst case 
// Space Complexity : O(logn) - recursive stack
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : 
 // 1. forgot to mention low < high in quicksort 
 // 2. in for loop kept till high - 1 important 

// Your code here along with comments explaining your approach


#include <iostream> 
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
    // take two indices i,j i starts from low-1 and j starts from low 
    // now j runs from low to high-1 and i only moves forward if arr[j]<=pivot
    //after i moving forward we swap arr[i] and arr[j] till j reaches high -1 
    // atleast we swap arr[i+1] with pivot beacause till i it is less than pivot 
    //from i+1 it is greater so swap i+1 an dpivot , and pivot position is i+ 1

    int pivot = arr[high]; // choosing pivot as last elemnt
    int i = low -1;    //keep tack of elements less than pivot

    for(int j = low; j <= high - 1 ; j++){ //till last but element as last is pivot
        if(arr[j] <= pivot){//found element less than pivot 
            i++; //and it should be placed at ith index increasing only when we see a element less than pivot
            swap(&arr[i], &arr[j]); 
        }
    }
    swap(&arr[i+1], &arr[high]); // placing pivot in correct position
    return (i+1);
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
    if(low < high){ 
        //low = high only one element sorted
        // low > high invalid or empty subarray nothing to sort
        int pivot = arr[high];
        int piv_point = partition(arr, low, high);
        quickSort(arr, low, piv_point - 1); // sorting left array
        quickSort(arr, piv_point + 1, high); //sorting right array
    }
    
    //Your Code here 
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