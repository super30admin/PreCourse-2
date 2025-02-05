// Time Complexity : O(nlogn) This is the expected case, assuming that the pivot is selected randomly or near-optimal. Again, the partitioning will divide the array into two roughly equal parts.
//Each recursive call processes O(n) elements, and the total number of recursive calls is O(log n), resulting in an average time complexity of O(n log n).
// Space Complexity : O(logn) The space complexity of QuickSort is determined by the depth of the recursion stack. In the best and average case, the partitioning results in approximately log(n) recursive calls.
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach


class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[], int i, int j) {
        // Swapping elements at indices i and j
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) { 
        // Pivot is chosen to be the last element
        int pivot = arr[high];
        int i = (low - 1); // index of smaller element

        // Traverse through all elements
        for (int j = low; j < high; j++) {
            // If current element is smaller than or equal to the pivot
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j); // Swap elements
            }
        }
        
        // Swap pivot element with element at index i + 1
        swap(arr, i + 1, high);
        return i + 1; // Return the pivot index
    } 
    
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) {  
        if (low < high) {
            // pi is partitioning index, arr[pi] is now at the correct position
            int pi = partition(arr, low, high);

            // Recursively sort elements before and after partition
            sort(arr, low, pi - 1);  // Sort left subarray
            sort(arr, pi + 1, high); // Sort right subarray
        }
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) { 
        int n = arr.length; 
        for (int i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  
    // Driver program 
    public static void main(String args[]) { 
        int arr[] = {10, 7, 8, 9, 1, 5}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n - 1); 
  
        System.out.println("Sorted array:"); 
        printArray(arr); 
    } 
}
