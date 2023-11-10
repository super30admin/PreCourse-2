// Time Complexity :O(nlog(n))
// Space Complexity :O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // Your code here
        int s1 = m - l + 1;
        int s2 = r - m;
        int a[] = new int[s1];
        int b[] = new int[s2];
        for (int i = 0; i < s1; i++)
            a[i] = arr[l + i];
        for (int j = 0; j < s2; j++)
            b[j] = arr[m + 1 + j];
        int i = 0, j = 0;

        // Initial index of merged subarry array
        int k = l;
        while (i < s1 && j < s2) {
            if (a[i] <= b[j]) {
                arr[k] = a[i];
                i++;
            } else {
                arr[k] = b[j];
                j++;
            }
            k++;
        }

        while (i < s1) {
            arr[k] = a[i];
            i++;
            k++;
        }

        while (j < s2) {
            arr[k] = b[j];
            j++;
            k++;
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