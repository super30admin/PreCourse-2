// Time Complexity : O(n log n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : NA
// Any problem you faced while coding this : Had to lookup old mergeSort program to brush up
class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {

        // initialize temp arrays with first part and second part
        int left[] = new int[m - l + 1];
        int right[] = new int[r - m];

        for (int i = 0; i < left.length; i++) {
            left[i] = arr[l + i];
        }
        for (int j = 0; j < right.length; j++) {
            right[j] = arr[m + 1 + j];
        }

        int i = 0, j = 0;

        // maintain new low for merging the two temp arrays
        int k = l;

        // compare and merge the 2 temp arrays
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                // console.log("🚀 ~ file: Exercise_4.java ~ line 26 ~ MergeSort ~ voidmerge ~
                // right[j]", right[j]);
                // console.log("🚀 ~ file: Exercise_4.java ~ line 26 ~ MergeSort ~ voidmerge ~
                // left[i]", left[i]);
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
            }
        }
        while (i < left.length) {
            arr[k++] = left[i++];
        }
        while (j < right.length) { // add remaining items from right array
            arr[k++] = right[j++];
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        if (l < r) {
            int mid = l + (r - l) / 2;

            sort(arr, l, mid);
            sort(arr, mid + 1, r);

            merge(arr, l, mid, r);
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