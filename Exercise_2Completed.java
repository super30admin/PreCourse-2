class QuickSort { 
    /* This function swaps the elements at indices i and j in the array arr */
    void swap(int arr[], int i, int j) {
        int temp = arr[i]; // Store the element at index i in a temporary variable
        arr[i] = arr[j]; // Copy the element at index j to index i
        arr[j] = temp; // Copy the temporary variable to index j
    }
    
    /* This function takes the last element as pivot, places the pivot element at its correct 
       position in sorted array, and places all smaller elements to left of pivot and all 
       greater elements to right of pivot */
    int partition(int arr[], int low, int high) {
        int pivot = arr[high]; // Choose the last element as the pivot
        int i = (low - 1); // Index of the smaller element
        
        for (int j = low; j < high; j++) {
            // If the current element is smaller than or equal to the pivot
            if (arr[j] <= pivot) {
                i++; // Increment index of the smaller element
                swap(arr, i, j); // Swap the current element with the element at index i
            }
        }
        
        swap(arr, i + 1, high); // Swap the pivot element with the element at index i+1
        return i + 1; // Return the partitioning index
    }
    
    /* The main function that implements QuickSort
       arr[] --> Array to be sorted
       low --> Starting index
       high --> Ending index */
    void sort(int arr[], int low, int high) {
        if (low < high) {
            // pi is partitioning index, arr[pi] is now at right place
            int pi = partition(arr, low, high);
            
            // Recursively sort elements before partition and after partition
            sort(arr, low, pi - 1);
            sort(arr, pi + 1, high);
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
  
        System.out.println("sorted array");
        printArray(arr);
    }
}
