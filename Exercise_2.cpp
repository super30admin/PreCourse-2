// Time Complexity : O(nlogn)  avg. and O(n^2) in worst case
// Space Complexity : O(1)  

/*
QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element 
as a pivot and partitions the given array around the picked pivot by placing the pivot 
in its correct position in the sorted array.
*/


#include <iostream>
#include <algorithm> 
using namespace std;  
  
// A utility function to swap two elements  
void swap(int* a, int* b)  
{  
    //Your Code here 
    int temp = *a;
    *a = *b;
    *b = temp;
    return;
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
    int i = low;
    for(int j=low; j<high; j++){
        if(arr[j] < pivot){
            swap(&arr[j], &arr[i]);
            i++;
        }
    }
    swap(&arr[i], &arr[high]);
    return i;


}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
    //Your Code here 
    if(low>= high) return;

    int pi = partition(arr, low, high);
    quickSort(arr, low, pi-1);
    quickSort(arr, pi+1, high);
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



// Apporach 2 :  using vector instead of Int array


#include <iostream>
#include <vector>

using namespace std;


int partition(std::vector<int> &arr, int low, int high){
    int i = low;
    int pivot = arr[high];
    
    for(int j=low; j<high; j++){
        if(arr[j] < pivot){
            std::swap(arr[j], arr[i]);     // in built function can be used to swap elemenrts in STL container
            i++;
        }
    }
    std::swap(arr[i], arr[high]);
    return i;
}

void quickSort(std::vector<int> &arr, int low, int high){
    if(low >= high) return;
    
    int pi = partition(arr, low, high);
    quickSort(arr, low, pi-1);
    quickSort(arr, pi+1, high);
}

int main() {
    
    std::vector<int>arr = {9,3,5,7,6,2,1};
    quickSort(arr, 0, arr.size()-1);
    
    std::cout << "sorted array is = " ;
    for(auto i : arr){
        std::cout << i << " ";
    }

    return 0;
}