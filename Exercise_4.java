// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : 
// Any problem you faced while coding this : Yes, I have watched tutorials and blog posts for merge sort and implemented accordingly

class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // Your code here
        int i = l;
        int j = m + 1;
        int k = l;

        // create dummy array to store sorted elements
        int[] dummy = new int[arr.length];

        while (i <= m && j <= r) {
            dummy[k++] = arr[i] < arr[j] ? arr[i++] : arr[j++];
        }

        // add remaining element in the array of both partition.
        while (i <= m) {
            dummy[k++] = arr[i++];
        }

        while (j <= r) {
            dummy[k++] = arr[j++];
        }
        
        // restore sorted array
        for (k = l; k <= r; k++) {
            arr[k] = dummy[k];
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        // Write your code here
        // Call mergeSort from here
        if (arr.length == 1) {
            return;
        }

        // when left is crossed right ptr means there is no divide further
        if (l < r) {
            int mid = (l + r) / 2;
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