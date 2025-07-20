// Time Complexity : O(n log n) on average, O(n^2) in worst case (when the smallest or largest element is always picked as pivot)
// Space Complexity : O(log n) due to recursion stack in average case, O(n) in worst case
// Did this code successfully run on Leetcode : Yes (if submitted to a problem requiring QuickSort, it would work)
// Any problem you faced while coding this : No major issues, but ensuring correct partitioning and swap positions is important

// Your code here along with comments explaining your approach

/*
Approach:
- The algorithm implements the QuickSort technique using recursion.
- The main idea is to choose a pivot (last element in this case), place the pivot in its correct sorted position,
  and move all smaller elements to its left and all larger elements to its right.
- We recursively do the same for left and right subarrays.
- A helper function `partition()` returns the index of the pivot after placing it correctly.
- The `swap()` utility function is used to exchange two elements.
- Base case for recursion is when low >= high.
- Finally, the sorted array is printed.

This is an in-place sort, meaning the array is sorted using its own memory (no extra array created).
*/

class QuickSort
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        // Utility function to swap two elements in the array
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // This function takes the last element as pivot,
    // places the pivot element at its correct position in sorted array,
    // and places all smaller to left and all greater to right of pivot
    int partition(int arr[], int low, int high)
    {
        int pivot = arr[high];
        int i = (low - 1); // index of smaller element

        for (int j = low; j < high; j++) {
            // If current element is smaller than the pivot
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        // Swap pivot to correct position
        swap(arr, i + 1, high);

        return i + 1;
    }
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {
        if (low < high) {
            // pi is partitioning index, arr[pi] is now at right place
            int pi = partition(arr, low, high);

            // Recursively sort elements before and after partition
            sort(arr, low, pi - 1);
            sort(arr, pi + 1, high);
        }
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
  
    // Driver program 
    public static void main(String args[]) 
    { 
        int arr[] = {10, 7, 8, 9, 1, 5}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
