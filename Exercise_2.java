// Time Complexity: O(n log n) on average, O(n^2) in the worst case
// Space Complexity: O(log n) for recursive stack space
// This is an implementation of the QuickSort algorithm in Java
// It sorts an array in ascending order using the QuickSort algorithm

class QuickSort 
{ 
    /* This function swaps two elements in the array */
    void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    /* This function takes the last element as pivot, places the pivot element at its correct 
       position in the sorted array, and places all smaller elements to the left of the pivot 
       and all greater elements to the right of the pivot */
    int partition(int arr[], int low, int high) { 
        int pivot = arr[high]; 
        int i = (low - 1); // Index of smaller element
        
        for (int j = low; j < high; j++) {
            // If the current element is smaller than or equal to the pivot
            if (arr[j] <= pivot) {
                i++;
                // Swap arr[i] and arr[j]
                swap(arr, i, j);
            }
        }
        
        // Swap arr[i+1] and arr[high] (or pivot)
        swap(arr, i + 1, high);
        
        return i + 1;
    } 
    
    /* The main function that implements QuickSort
       arr[] --> Array to be sorted, 
       low  --> Starting index, 
       high  --> Ending index */
    void sort(int arr[], int low, int high) {  
        if (low < high) {
            // Partition the array around the pivot
            int pi = partition(arr, low, high);
            
            // Recursively sort elements before and after partition
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
