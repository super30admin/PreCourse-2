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
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high) {
        // Write code here for Partition and Swap
        int pivot = arr[low];
        int count = 0;
        for (int i = low + 1; i <= high; i++) {
            if (arr[i] <= pivot)
                count++;
        }
        int pivotIndex = low + count;
        swap(arr, low, pivotIndex);
        int i = low, j = high;
        while (i < pivotIndex && j > pivotIndex) {
            while (arr[i] <= pivot) {
                i++;
            }
            while (arr[j] > pivot) {
                j--;
            }
            if (i < pivotIndex && j > pivotIndex) {
                swap(arr, i, j);
                i++;
                j--;
            }
        }
        return pivotIndex;
    }

    /*
     * The main function that implements QuickSort()
     * arr[] --> Array to be sorted,
     * low --> Starting index,
     * high --> Ending index
     */
    void sort(int arr[], int low, int high) {
        if (low >= high)
            return;
        int p = partition(arr, low, high);

        sort(arr, low, p - 1);
        sort(arr, p + 1, high);
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
}

public class Exercise_2 {
    // Driver program
    public static void main(String args[]) {
        int arr[] = { 10, 7, 8, 8, 9, 1, 5, 6, 2 };
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);

        System.out.println("sorted array");
        ob.printArray(arr);
    }
}
