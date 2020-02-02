// Time Complexity :O(nlogn)
// Space Complexity : no extra space needed except for variables. doing in place sort
class QuickSort {
    /*
     * This function takes last element as pivot, places the pivot element at its
     * correct position in sorted array, and places all smaller (smaller than pivot)
     * to left of pivot and all greater elements to right of pivot
     */
    void swap(int arr[], int i, int j) {
        // Your code here
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high) {
        // Write code here for Partition and Swap
        // taking last element as pivot
        int pivot = arr[high];
        int i = low;
        int j = high;
        while (true) { // running the loop untill i < j
            while (arr[j] > pivot) // decreasing right pointer until we reach an element lesser than pivot
                j--;
            while (arr[i] < pivot) // increasing left pointer until we reach an element greater than pivot
                i++;
            if (i < j) // swapping the places of the elements at i and j
                swap(arr, i, j);
            else
                return j; // returning the index where the next partition should happen
        }
    }

    /*
     * The main function that implements QuickSort() arr[] --> Array to be sorted,
     * low --> Starting index, high --> Ending index
     */
    void sort(int arr[], int low, int high) {
        if (low < high) {
            // Changing the pivot to its right place and
            // returning the correct place of pivot
            int part = partition(arr, low, high);
            // Recursively sort elements before
            // partition and after partition
            sort(arr, low, part - 1);
            sort(arr, part + 1, high);
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
        int arr[] = { 10, 7, 8, 9, 1, 5, 5 };
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);

        System.out.println("sorted array");
        printArray(arr);
    }
}
