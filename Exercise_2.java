//Time Complexity: Best case-O(nlog n), Worst case-O(n^2)
//Space complexity: Best case-O(log n), Worst case-O(n)
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
        // Swap 2 elements in an array
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    }

    int partition(int arr[], int low, int high) {
        int pivot = arr[high];
        int pindex = low;
        // Traverse through array and place elements less than pivot to the left
        for (int i = low; i < high; i++) {
            if (arr[i] < pivot) {
                swap(arr, i, pindex);// swap current element with element at pindex
                pindex++;
            }
        }
        // swap the pivot to its corrected sorted position
        swap(arr, pindex, high);
        return pindex;

    }

    /*
     * The main function that implements QuickSort()
     * arr[] --> Array to be sorted,
     * low --> Starting index,
     * high --> Ending index
     */
    void sort(int arr[], int low, int high) {
        if (low < high) {
            // get pivot index by partitioning the array
            int p = partition(arr, low, high);
            // Sort the elements on the left of pivot recursively.
            sort(arr, low, p - 1);
            // Sort the elements on the right of pivot recursively.
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
