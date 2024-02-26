// Time Complexity : O(n log n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // Find length of the 2 arrays
        int len1 = m - l + 1;
        int len2 = r - m;

        // temporary arrays
        int arr1[] = new int[len1];
        int arr2[] = new int[len2];

        for (int i = 0; i < len1; ++i) {
            arr1[i] = arr[l + i];
        }
        for (int i = 0; i < len2; ++i) {
            arr2[i] = arr[m + 1 + i];
        }

        // Merging the arrays
        int index1 = 0;
        int index2 = 0;
        int k = l;
        while (index1 < len1 && index2 < len2) {
            if (arr1[index1] <= arr2[index2]) {
                arr[k] = arr1[index1];
                index1++;
            } else {
                arr[k] = arr2[index2];
                index2++;
            }
            k++;
        }

        // copy remaining elements
        while (index1 < len1) {
            arr[k] = arr1[index1];
            index1++;
            k++;
        }
        while (index2 < len2) {
            arr[k] = arr2[index2];
            index2++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        // Write your code here
        if (l < r) {
            int mid = l + (r - l) / 2; // Find middle point
            sort(arr, l, mid); // Sort first half
            sort(arr, mid + 1, r); // Sort first half
            merge(arr, l, mid, r); // Call mergeSort from here
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