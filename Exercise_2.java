// Time Complexity: O(NLogN) but worst case would be O(n^2) if we take array in decreasing order
// Space Complexity: O(NLogn) and worst case would be 
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach


class QuickSort { 
    /* This function swaps two elements in the array */
    void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /* This function takes the last element as pivot,
       places it at its correct position in the sorted array,
       and moves smaller elements to the left and greater ones to the right */
    int partition(int arr[], int low, int high) { 
        int pivot = arr[high];  // Pivot element
        int swapIndex = low;  

        for (int i = low; i < high; i++) {
            if (arr[i] <= pivot) {  // Elements smaller than pivot
                swap(arr, i, swapIndex);
                swapIndex++;
            }
        }
        
        // Swap pivot to its correct position
        swap(arr, swapIndex, high);
        return swapIndex; 
    } 

    /* The main function that implements QuickSort */
    void sort(int arr[], int low, int high) {  
        if (low < high) { 
            int partitionIndex = partition(arr, low, high); 

            // Recursively sort elements before and after partition
            sort(arr, low, partitionIndex - 1); 
            sort(arr, partitionIndex + 1, high); 
        } 
    } 

    /* A utility function to print an array */
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
  
        System.out.println("Sorted array"); 
        printArray(arr); 
    } 
}
