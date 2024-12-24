class QuickSort 
{
    // Time Complexity: O(NlogN)  - O(n) to position the pivot and O(logN) called recursively on left and right sub arrays
    // Space Complexity: O(1)
    // Did this code successfully run on Leetcode : Passed 17/21 test cases for this problem = https://leetcode.com/problems/sort-an-array/description/?envType=problem-list-v2&envId=merge-sort
    // Any problem you faced while coding this : Yes, with coding the partition and finding which is the boundary index for smaller element

    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int[] arr, int i, int j){
        //Your code here
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int partition(int[] arr, int low, int high)
    { 
   	    //Write code here for Partition and Swap
        int pivot = arr[high];
        int i = low - 1; // pointer for tracking smaller elements
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i+1, high); // pivot should be placed immediately after smaller elements,
        // so it is i+1 to ensure smaller elements are placed left
        return i+1;
    }

    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int[] arr, int low, int high)
    {
        // Recursively sort elements before
        // partition and after partition
        if (low >= high) // base case: if at any moment low is equal to or greater than high, return
            return;
        int pivotIndex = partition(arr, low, high);
        sort(arr, low, pivotIndex - 1); // sort left array to partition
        sort(arr, pivotIndex + 1, high); // sort right array to partition
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int[] arr)
    {
        for (int j : arr) System.out.print(j + " ");
        System.out.println(); 
    } 
  
    // Driver program 
    public static void main(String[] args)
    { 
        int[] arr = {10, 7, 8, 9, 1, 5};
        int n = arr.length;
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
