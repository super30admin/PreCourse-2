// Time Complexity :O(nlogn) where n is no of elements
// Space Complexity :O(n)
// Did this code successfully run on Leetcode :NA
// Any problem you faced while coding this :had to study the algo to code, how it works

class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // we'll ahve three pointers for
        int i = l;
        int j = m + 1;
        int k = l;
        int[] temp = new int[arr.length];// we'll make a temp array so that we can store sorted version
        while (i <= m && j <= r) {// we'll traverse through first part(l to m) and second part ie m+1 to r
            if (arr[i] < arr[j]) {
                temp[k] = arr[i];// we'll store in temp array whichever is smaller and increment the pointers
                i++;
            } else {
                temp[k] = arr[j];
                j++;
            }
            k++;
        }
        // if one of the part of the array is left while other is completed, we'll copy
        // that in end of temp array
        // as array is sorted
        if (i > m) {
            while (j <= r) {
                temp[k] = arr[j];
                k++;
                j++;
            }
        } else {
            while (i <= m) {
                temp[k] = arr[i];
                k++;
                i++;
            }
        }
        // we'll copy temp array in main array
        for (int newPtr = l; newPtr <= r; newPtr++) {
            arr[newPtr] = temp[newPtr];
        }
        // Your code here
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        if (l < r) {// if we have atleast two elements in array
            int mid = l + (r - l) / 2;// find mid
            sort(arr, l, mid);// sort for l to mid
            sort(arr, mid + 1, r);// sort mid+1 to r
            merge(arr, l, mid, r);// merge both
        }
        // Write your code here
        // Call mergeSort from here
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
