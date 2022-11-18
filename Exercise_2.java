// Time Complexity : O(nlogn) 

// Space Complexity : O(logn) -> recursive call

// Did this code successfully run on Leetcode : yes

// Any problem you faced while coding this :
// read the concept and working of QuickSort

// Your code here along with comments explaining your approach
/* we select last element as pivot element. Once pivot assigned, set i as low and j as high index.
 * increment index through the array from left(i) till we find a greater value than pivot and decrement index from right(j) till we find a smaller value than pivot.
 * if we find smaller and greater value we swap i and j. if i and j cross each other we swap the pivot value with the j index and return the j value as partition index.
 * Then we sort the remaining by using the partition index.
 */

class QuickSort {
    /*
     * This function takes last element as pivot,
     * places the pivot element at its correct
     * position in sorted array, and places all
     * smaller (smaller than pivot) to left of
     * pivot and all greater elements to right
     * of pivot
     */
    // assign a temporary variable to swap 2 variable.
    void swap(int arr[], int i, int j) {
        // Your code here
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high) {
        // Write code here for Partition and Swap
        // as mentioned assigned last element as pivot.
        int pivot = arr[high];
        int i = low, j = high;
        // iterate through the array till i and j don't intersect with each other.
        while (i < j) {

            // increment i till we find a value greater than pivot element
            while (arr[i] <= pivot && i < j) {
                i++;
            }

            // decrement j till we find value smaller than pivot element
            while (arr[j] >= pivot && i < j) {
                j--;
            }

            // swap element at index i and j
            swap(arr, i, j);
        }

        // swap element at i and high(pivot) to get the partition index
        swap(arr, i, high);

        return i;
    }

    /*
     * The main function that implements QuickSort()
     * arr[] --> Array to be sorted,
     * low --> Starting index,
     * high --> Ending index
     */
    void sort(int arr[], int low, int high) {
        // run till low and high intersect
        if (low < high) {
            int j = partition(arr, low, high);
            // sort the left and right side of the partition index.
            sort(arr, low, j - 1);
            sort(arr, j + 1, high);
        }
        // Recursively sort elements before
        // partition and after partition
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
