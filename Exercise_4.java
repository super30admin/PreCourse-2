// Time Complexity  : O(n log n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes (https://leetcode.com/problems/sort-an-array/)
// Any problem you faced while coding this : no

class MergeSort {

    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        int len1 = m - l + 1;
        int len2 = r - m;

        int[] arr1 = new int[len1];
        int[] arr2 = new int[len2];

        for (int i = 0; i < len1; i++) {
            arr1[i] = arr[l + i];
        }
        for (int j = 0; j < len2; j++) {
            arr2[j] = arr[m + 1 + j];
        }
        int i = 0, j = 0, k = l;
        while (i < len1 && j < len2) {
            if (arr1[i] <= arr2[j]) {
                arr[k++] = arr1[i++];
            } else {
                arr[k++] = arr2[j++];
            }
        }
        while (i < len1) {
            arr[k++] = arr1[i++];
        }
        while (j < len2) {
            arr[k++] = arr2[j++];
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
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
        int arr[] = {12, 11, 13, 5, 6, 7};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
} 