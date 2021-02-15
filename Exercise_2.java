// Time Complexity:
// Best Case : Assuming the partition is always done in the middle, the time complexity is O(nlogn). At each partition level it takes 
// O(n) time and there are log n such levels. So the overall time complexity is O(nlogn)
// Worst Case : If the partition always happen at the beginning or end of the array, then the time complexity is O(n^2)

// Space Complexity : O(1)

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
        int pivot = arr[low];
        int start = low, end = high;

        while (start < end) {
            while (start <= high && arr[start] <= pivot)
                start++;
            while (end >= low && arr[end] > pivot)
                end--;
            if (start < end) {
                swap(arr, start, end);
            }
        }
        swap(arr, low, end);
        return end;
    }

    /*
     * The main function that implements QuickSort() arr[] --> Array to be sorted,
     * low --> Starting index, high --> Ending index
     */
    void sort(int arr[], int low, int high) {
        // Recursively sort elements before
        // partition and after partition
        if (low < high) {
            int pivotIndex = partition(arr, low, high);

            sort(arr, low, pivotIndex - 1);
            sort(arr, pivotIndex + 1, high);
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
