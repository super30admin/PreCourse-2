// Time Complexity : average case: O(N logN) Worst case O(n2)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : yES
// Any problem you faced while coding this : No

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
        int temp = arr[i]; // temporary var
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high) {

        int pivot = arr[high]; // setting the pivot to last element of the array
        int i = low - 1; // starting i from left side, if it starts from 0 then proper swap wont be done as well as check.

        for (int j = low; j <= high - 1; j++) { // shifting all numbers less than pivot to left side
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }

        }
        swap(arr, i + 1, high); // finally swapping pivot and ith position, therby cementing the pivots position
        return i + 1; // return the index of pivot
    }

    /*
     * The main function that implements QuickSort()
     * arr[] --> Array to be sorted,
     * low --> Starting index,
     * high --> Ending index
     */
    void sort(int arr[], int low, int high) {

        if (low <= high) {
            int pivot = partition(arr, low, high);
            sort(arr, low, pivot - 1);
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
