class QuickSort {
    // Time Complexity : O(n * log n) Avg, Worst: O(n^2)
    // Space Complexity : O(log n)
    // Did this code successfully run on Leetcode : N/A
    // Any problem you faced while coding this : None


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

    int partition(int arr[], int low, int high) {
   	    //Write code here for Partition and Swap
//        ==================== when pivot is last element of array ====================
        int pivot = arr[high];
        int i = low - 1; // assuming all elements are greater than pivot

        // iterate through array to find elements smaller than pivot and place them in correct position
//         loop will run through last-1 element as last element is pivot
        for(int j = low; j < high; j++){
            // element at j is smaller than pivot, swap with i
            if(pivot > arr[j]) {
                // increment i so we can swap
                i++;
                swap(arr, i, j);
            }
        }
        i++; // increment i, to swap with pivot. As i is the correct index for pivot
        swap(arr, i, high);
        return i;
//       ================================================================================

        // ==================== when pivot is first element of array ====================
//        int pivot = arr[low];
//        int i = low;
//        int j = high;
//
//        while(j > i){
//            while(i <= j && arr[i] <= pivot){
//                i++;
//            }
//
//            while(i <=j && arr[j] > pivot){
//                j--;
//            }
//
//            if(j >= i){
//                swap(arr, i, j);
//            }
//        }
//        if(i > j){
//            swap(arr, low, j);
//        }
//        return j;
//        ================================================================================

    }
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) {
            // Recursively sort elements before 
            // partition and after partition
        // start if there is atleast 2 elements in arr
        if(low < high) {
            int j = partition(arr, low, high);
            sort(arr, low, j-1); // apply quicksort on left side of partition index
            sort(arr, j + 1, high); // apply quicksort on right side of partition index
        }
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) {
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
  
    // Driver program 
    public static void main(String args[]) {
        int arr[] = {10, 7, 8, 9, 1, 5}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
