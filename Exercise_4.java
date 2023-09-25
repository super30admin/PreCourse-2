/**
 * TC: O(n log n) <br>
 * SC: O(n)
 */
public class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r, int[] temp) {
        // Your code here
        int i = l;
        int j = m + 1;
        int index = 0;
        while (i <= m && j <= r) {
            if (arr[i] <= arr[j]) {
                temp[index++] = arr[i++];
            } else {
                temp[index++] = arr[j++];
            }
        }
        while (i <= m) {
            temp[index++] = arr[i++];
        }
        while (j <= r) {
            temp[index++] = arr[j++];
        }
        index = 0;
        while (l <= r) {
            arr[l++] = temp[index++];
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r, int[] temp) {
        // Write your code here
        // Call mergeSort from here
        if (l >= r) {
            return;
        }
        int mid = l + (r - l) / 2;
        sort(arr, l, mid, temp);
        sort(arr, mid + 1, r, temp);
        merge(arr, l, mid, r, temp);
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
        ob.sort(arr, 0, arr.length - 1, new int[arr.length]);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}