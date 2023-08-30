class QuickSort {

    void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return i + 1;
    }

    void sort(int arr[], int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);

            // Recursively sort the elements before and after the partition
            sort(arr, low, pi - 1);
            sort(arr, pi + 1, high);
        }
    }

    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String args[]) {
        int arr[] = { 10, 7, 8, 9, 1, 5 };
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);

        System.out.println("Sorted array:");
        printArray(arr);
    }
}

// Time Complexity:
// - Best Case: O(n log n)
// - Average Case: O(n log n)
// - Worst Case: O(n^2) [When the array is already sorted]
// Space Complexity:
// - In-place sorting, so O(log n) for the recursive stack
