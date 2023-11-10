// Time Complexity : Time complexity of quicksort is O(nLog(n)) for best case and average case and O(n^2) for worst case
// Space Complexity : There is extra space required due to recursion so space complexity is O(log(n)) and O(n) for  worst case
// Did this code successfully run on Leetcode : could not find it on leetcode
// Any problem you faced while coding this :
// Had to debug a lot to find problems in the algorithm
// Had to look up time and space complexity for quicksort
// Had to lookup quicksort as I could not recollect how quicksort worked

// Your code here along with comments explaining your approach

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
        // creating a temporary variable which will help in swapping the element
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high) {
        // Write code here for Partition and Swap
        // Variable pivot which is the last element in the array. Pivot will be used to
        // compare and divide the array in 2 parts
        int pivot = high;
        high--; // As pivot is the highest element, making the highest element as the one before
                // pivot
        // Lopp will run while the low and high pointer do not cross
        while (low <= high) {
            while (low <= high && arr[low] <= arr[pivot]) { // To find the element on the left side of the array to swap
                low++;
            }
            while (low <= high && arr[high] >= arr[pivot]) { // To find the element on the right side of the array to
                                                             // swap
                high--;
            }
            if (low <= high)
                swap(arr, high, low); // Swap the elements on left and right side
        }

        swap(arr, low, pivot); // Swap the elements to get the pivot element right in between the two parts of
                               // array
        return low;

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
            int p = partition(arr, low, high);
            sort(arr, low, p - 1);
            sort(arr, p + 1, high);
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
