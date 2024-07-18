// Time Complexity : O(nLogN)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // Your code here
        int ln = m - l + 1;
        int rn = r - m;

        int[] lArr = new int[ln];
        int[] rArr = new int[rn];

        for (int i = 0; i < ln; i++) {
            lArr[i] = arr[l + i];
        }
        for (int j = 0; j < rn; j++) {
            rArr[j] = arr[m + 1 + j];
        }

        int i = 0, j = 0;

        int k = l;
        while (i < ln && j < rn) {
            if (lArr[i] < rArr[j]) {
                arr[k] = lArr[i++];
            } else {
                arr[k] = rArr[j++];
            }
            k++;
        }

        while (i < ln) {
            arr[k++] = lArr[i++];
        }

        while (j < rn) {
            arr[k++] = rArr[j++];
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