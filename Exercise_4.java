// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : 
// Any problem you faced while coding this : Yes, I have seen some youtube videos to understand merge sort algorithm and done coding

class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // intialize i with l for traversal of first partition
        int i = l;
        // intialize j with m+1 for traversal of second partition
        int j = m + 1;

        // use k pointer for storing sorted data in temp array
        int k = l;

        // create temp array to store sorted elements
        int[] temp = new int[arr.length];

        // compare two partition and add small element in the temp array.
        while (i <= m && j <= r) {
            temp[k++] = arr[i] < arr[j] ? arr[i++] : arr[j++];

        }
        // add remaining element in the array of both partition.
        while (i <= m) {
            temp[k++] = arr[i++];
        }
        while (j <= r) {
            temp[k++] = arr[j++];
        }
        // restore sorted array
        for (k = l; k <= r; k++) {
            arr[k] = temp[k];
        }

    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        // Write your code here
        // Call mergeSort from here
        // if l > r it means there is no further dividing. So, we are not going to
        // divide further.
        if (l < r) {

            // find the mid element and divide the array.
            int mid = (l + r) / 2;

            // divide into first half
            sort(arr, l, mid);
            // divide into second half
            sort(arr, mid + 1, r);

            // merge divided array
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
        int arr[] = { 12, 11, 13, 5, 6, 7, 21, 23, 54 };

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}