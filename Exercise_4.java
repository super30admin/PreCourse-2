// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach

class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // Your code here
        // length of 2 arrays l to m and m + 1 to r
        int p1 = m - l + 1;
        int p2 = r - m;

        // create 2 temp arrays to merge
        int arr1[] = new int[p1];
        int arr2[] = new int[p2];

        // copy 1st half to arr1
        for (int l1 = 0; l1 < p1; l1++) {
            arr1[l1] = arr[l + l1];
        }
        // copy 2nd half to arr2
        for (int l1 = 0; l1 < p2; l1++) {
            arr2[l1] = arr[m + 1 + l1];
        }

        // assign index i and j = 0 to interate through arr1 and arr2.
        // assign variable k as l add the values to arr. k = l because we will get
        // arrays with different lengths and starting point would vary.
        int i = 0, j = 0, k = l;

        // run the while loop till both the indexes are less than arr1 and arr2 lengths
        // check the smaller value and add it to the main array arr.
        while (i < p1 && j < p2) {
            if (arr1[i] <= arr2[j]) {
                arr[k] = arr1[i];
                i++;
            } else {
                arr[k] = arr2[j];
                j++;
            }
            k++;
        }

        // add remaining values directly to the array.
        while (i < p1) {
            arr[k] = arr1[i];
            i++;
            k++;
        }
        while (j < p2) {
            arr[k] = arr2[j];
            j++;
            k++;
        }

    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        // Write your code here
        // Call mergeSort from here
        // divide the array and recursively call the sort function . At the end call the
        // merge function.
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