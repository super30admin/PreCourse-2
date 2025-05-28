// Time Complexity : 
//    Average Case: O(n log n) — The array is divided roughly in half each time.
//    Worst Case: O(n^2) — When the pivot divides the array unevenly (e.g., sorted array).
// Space Complexity : O(log n) — Due to recursive stack space in average case.
// Did this code successfully run on Leetcode : Yes, this approach passes typical sorting problems also getting Time Limit Exceeded
// Any problem you faced while coding this : 
//    Understanding why start is initialized to low - 1 and handling pivot placement carefully.

class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) {
        int pivot = arr[high];        // pivot at the end
        int start = low - 1;          // boundary for smaller elements
        int end = low;

        while (end <= high - 1) {     // scan excludes pivot itself
            if (arr[end] <= pivot) {
                start++;
                swap(arr, start, end);
            }
            end++;
        }
        // place pivot after the last smaller element
        swap(arr, start + 1, high);

        return start + 1; // return pivot's correct position
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
            int pi = partition(arr, low, high);
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
