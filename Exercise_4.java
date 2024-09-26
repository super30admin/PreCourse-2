/**
 * Time Complexity : O(n log n)
 * Space Complexity: O(n)
 * Did this code successfully run on Leetcode : Yes, https://leetcode.com/problems/sort-an-array/
 *
 * Any problem you faced while coding this : NA
 */
class MergeSort {
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int[] arr, int l, int m, int r) {
        //Your code here
        int s1 = m - l + 1;
        int s2 = r - m;
        int[] left = new int[s1];
        int[] right = new int[s2];
        for (int i = 0; i < s1; ++i)
            left[i] = arr[l + i];
        for (int j = 0; j < s2; ++j)
            right[j] = arr[m + 1 + j];
        int i = 0, j = 0, k = l;
        while (i < s1 && j < s2) {
            if (left[i] >= right[j])
                arr[k++] = right[j++];
            else
                arr[k++] = left[i++];
        }
        while (i < s1)
            arr[k++] = left[i++];

        while (j < s2)
            arr[k++] = right[j++];
    }

    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int[] arr, int l, int r) {
        //Write your code here
        //Call mergeSort from here
        if (l < r) {
            int middle = l + (r - l) / 2;
            sort(arr, l, middle);
            sort(arr, middle + 1, r);
            merge(arr, l, middle, r);
        }

    }

    /* A utility function to print array of size n */
    static void printArray(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver method 
    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6, 7};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
} 