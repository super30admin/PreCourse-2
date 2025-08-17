/*
TC: Best/Average Case -> O(nlogn), Worst Case -> O(n^2)
In the best case, the pivot selection will be such that the array is split into halves each time. So if we split into half at each level, the 
recursion tree will have a depth of log n. At each step the work done is n. Since we scan/swap over the entire array at each level. Even if we split
the arrays into smaller subarrays, the total work done for all subarrays on the same level = n. Therefore the best case TC is O(nlogn).
For average case, we might not get a clean half split, but we can still expect a reasonably balanced/non-skewed split. The TC for this case still
ends up about O(nlogn).

The worst case happens when the pivot selection is bad, either the smallest or the largest element in the subarray is picked as pivot. What this does
is that the partitioned subarrays have lengths [n-1] & 0. This leads to a very skewed recursion tree (n -> n-1 -> n-2 -> n-3 ...). The depth of this
tree will be n. The work done at each level still is n. Therefore, the worst case TC becomes O(n^2).

SC: Best/Average case: O(logn) -> There is no extra space needed as we swap in place in the same array. The space consumed is due to the recursion
stack, which is log n in the best/average case as explained above.
For the worst case, since the recursion tree is skewed and resembles a linkedlist/chain type structure, the depth = n. So the SC becomes O(n).

Explanation in Sample.java
*/

#include <bits/stdc++.h> 
using namespace std;  
  
// A utility function to swap two elements  
void swap(int* a, int* b) 
{ 
    if(*a == *b) return;
    *a = *a + *b;
    *b = *a - *b;
    *a = *a - *b;
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
    int i = low; // iterator for the left partition
    int j = high; // iterator for the right partition
    while(i < j){ // to ensure that the left & right iterators don't cross each other 
        while(i<=high && arr[i] < pivot){ // find first element in the left partition which does not satisfy our constraints
            i++;
        }
        while(j>=low && arr[j] >= pivot) { // find first element in the right partition which does not satisfy our constraints
            j--;
        }
        if(i < j){ // to make sure that the swap is still valid (we don't want to accidentally swap elements which are in the correct partition)
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i], &arr[high]); // the index where the left iterator spills into the right partition will be the correct position of the pivot
    return i; // return index of pivot
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
    //Your Code here 
    if(low < high) { // atleast 2 elements need to be present to continue, 1 element by itself is considered sorted
        int pIndex = partition(arr, low, high);
        quickSort(arr, low, pIndex-1); 
        quickSort(arr, pIndex+1, high);
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

bool isSorted(int A[], int size) {
    for(int i=1; i<size; i++){
        if(A[i-1] > A[i]) return false;
    }
    return true;
}
  
// Driver Code 
int main()  
{  
    /* TEST CASES */
    int arr[] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};  
    // int arr[] = {}; // empty array
    // int arr[] = {1}; // array with only one element (already sorted)
    // int arr[] = {1, 2, 3, 4}; // already sorted array
    // int arr[] = {1, 3, 2, 1, 2, 3, 4, 1, 4, 2, 3}; // array with duplicates
    // int arr[] = {5,-1,3,0,-2,4,-3}; // negatives
    // int arr[] = {INT_MIN, 0, INT_MIN, INT_MAX}; // extreme values

    int n = sizeof(arr) / sizeof(arr[0]);  
    
    if(n == 0) {
        cerr<<"Invalid array"<<endl;
        return 1;
    } 

    if(n == 1 || isSorted(arr, n)){
        cout<<"Array is already sorted."<<endl;
        return 0;
    } 

    quickSort(arr, 0, n - 1);  
    cout << "Sorted array: \n";  
    printArray(arr, n);  
    return 0;  
}  