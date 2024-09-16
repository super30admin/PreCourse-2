class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // Your code here
        int i, j, k;

        int left_array[] = new int[m - l + 1];
        i = 0;
        k = l;
        while (k <= m) {
            left_array[i++] = arr[k++];
        }

        int right_array[] = new int[r - m];
        j = 0;
        k = m + 1;
        while (k <= r) {
            right_array[j++] = arr[k++];
        }

        i = 0;
        j = 0;
        k = l;
        while (i < m - l + 1 && j < r - m) {
            if (left_array[i] <= right_array[j]) {
                arr[k++] = left_array[i++];
            } else {
                arr[k++] = right_array[j++];
            }
        }
        while (i < m - l + 1) {
            arr[k++] = left_array[i++];
        }
        while (j < r - m) {
            arr[k++] = right_array[j++];
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        // Write your code here
        // Call mergeSort from here
        if (l < r) {
            int m = l + (r - l) / 2;
            sort(arr, l, m);
            sort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver method
    public static void main(String args[]) {
        int arr[] = { 12, 11, 13, 5, 6, 7 };

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}