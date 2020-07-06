/*Time Complexity : O(n log n)
 Space Complexity : O(n), because of using additional temp arrays

 Your code here along with comments explaining your approach:
 Using divide and conquer approach, divide the input array in the middle.
 Divide the array in left sub-array and right sub-array. Keep dividing the array
 until the array contains only 1 element. Sort the single element sub arrays and merge the sub arrays.
 It results in sorting the entire array.
*/
class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        int k = 0;
        int[] tempA = new int[m - l+1];
        int[] tempB = new int[r - m];
        /*Need to copy arr in temporary arrays*/
        for (int i = l; i <= m; i++) {
            tempA[k++] = arr[i];
        }
        k = 0;
        for (int i = m+1; i <= r; i++) {
            tempB[k++] = arr[i];
        }

        int i = 0, j = 0;
        k = l;
        /*comparing and copying whichever value is less*/
        for (; i < tempA.length && j < tempB.length; ) {
            if (tempA[i] <= tempB[j]) {
                arr[k++] = tempA[i++];
            } else {
                arr[k++] = tempB[j++];
            }
        }

        while (i < tempA.length) {
            arr[k++] = tempA[i++];
        }

        while (j < tempB.length) {
            arr[k++] = tempB[j++];
        }

    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
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
        int arr[] = {12, 11, 13, 5, 6, 7, 10, 8};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
} 