// Time Complexity :
//   Average  -> O(n log n)
//   Worst    -> O(n^2) (e.g., already sorted array with last-element pivot)
//   Best     -> O(n log n)
// Space Complexity :
//   Average  -> O(log n) due to recursion stack
//   Worst    -> O(n) recursion depth (highly unbalanced partitions)
// Any problem you faced while coding this :
//   - Off-by-one mistakes in partition (low, high, i, j pointers).
//   - Picking the last element as pivot can lead to worst-case on sorted input.
//   - Remember QuickSort is NOT stable.
// Did this code successfully run on Leetcode : NA
// Your code here along with comments explaining your approach:
//   - Use Lomuto partition scheme with the LAST element as pivot.
//   - Move all elements smaller than pivot to the left side by swapping as we scan.
//   - Finally put pivot in its correct place and then recursively sort left and right parts.
class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        //Your code here
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;   
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap
       int pivot = arr[high];    // pivot is the last element
       int i = low - 1;          // i points to the last index of "smaller than pivot" region

       for (int j = low; j <= high - 1; j++) {
           // If current element is smaller than pivot, expand the "smaller" region
           if (arr[j] < pivot) {
               i++;
               swap(arr, i, j);
           } 
    } 
    // Place pivot in its correct position (right after the "smaller" region)
    swap(arr, i + 1, high);
    return i + 1; // return pivot index
    }

    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        // Recursively sort elements before 
        // partition and after partition
        if (low < high) {
            // Partition the array and get pivot index
            int pi = partition(arr, low, high);

            // Recursively sort elements before and after pivot
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

