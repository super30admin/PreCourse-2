// Time Complexity : O(n logn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : NA
// Any problem you faced while coding this : Coming up with merge logic, especially while loops.

class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // Your code here
        int size1 = m - l + 1;
        int size2 = r - m;

        int left[] = new int[size1];
        int right[] = new int[size2];

        // Filling out dummy arrays
        for (int i = 0; i < size1; ++i)
            left[i] = arr[l + i];
        for (int j = 0; j < size2; ++j)
            right[j] = arr[m + 1 + j];

        int i = 0;
        int j = 0;

        int curr = l;
        while (i < size1 && j < size2) {
            if (left[i] <= right[j]) {
                arr[curr] = left[i];
                i++;
            } else {
                arr[curr] = right[j];
                j++;
            }
            curr++;
        }

        while (i < size1) {
            arr[curr] = left[i];
            i++;
            curr++;
        }

        while (j < size2) {
            arr[curr] = right[j];
            j++;
            curr++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        // Write your code here
        // Call mergeSort from here
        if (l < r) {
            // Finding middle index
            int midIndex = l + (r - l) / 2;

            // Sorting both the sides recursively
            sort(arr, l, midIndex);
            sort(arr, midIndex + 1, r);

            // Merging the result of above sort
            merge(arr, l, midIndex, r);
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