// Time Complexity : O(n^2)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : NA
// Any problem you faced while coding this : To figure out the recursion.

class QuickSort {
    /*
     * This function takes last element as pivot,
     * places the pivot element at its correct
     * position in sorted array, and places all
     * smaller (smaller than pivot) to left of
     * pivot and all greater elements to right
     * of pivot
     */
    void swap(int arr[], int i, int j) {
        // Your code here
        // We just swap the given elements here.
        int curr = arr[i];
        arr[i] = arr[j];
        arr[j] = curr;
    }

    int partition(int arr[], int low, int high) {
        // Write code here for Partition and Swap
        // pivot
        int pivot = arr[high];

        int i = low - 1;

        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                swap(arr, ++i, j);
            }
        }
        swap(arr, ++i, high);
        return i;
    }

    /*
     * The main function that implements QuickSort()
     * arr[] --> Array to be sorted,
     * low --> Starting index,
     * high --> Ending index
     */
    void sort(int arr[], int low, int high) {
        // Recursively sort elements before
        // partition and after partition
        if (low < high) {

            // Finding pivot
            int pivot = partition(arr, low, high);

            // Sorting left side of the pivot
            sort(arr, low, pivot - 1);

            // Sorting right side of the pivot
            sort(arr, pivot + 1, high);
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
        int arr[] = { 10, 7, 8, 9, 1, 5 };
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);

        System.out.println("sorted array");
        printArray(arr);
    }
}