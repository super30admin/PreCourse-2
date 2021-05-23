import java.util.Arrays;

class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // Create copies of sub arrays
        int leftSubArray[] = Arrays.copyOfRange(arr, l, m + 1);
        int leftIndex = 0;

        int rightSubArray[] = Arrays.copyOfRange(arr, m + 1, r + 1);
        int rightIndex = 0;

        // Sort and fill the main array
        while (leftIndex < leftSubArray.length && rightIndex < rightSubArray.length) {
            if (leftSubArray[leftIndex] <= rightSubArray[rightIndex]) {
                arr[l++] = leftSubArray[leftIndex++];
            } else {
                arr[l++] = rightSubArray[rightIndex++];
            }
        }

        // for remaining array items
        while (leftIndex < leftSubArray.length) {
            arr[l++] = leftSubArray[leftIndex++];
        }

        while (rightIndex < rightSubArray.length) {
            arr[l++] = rightSubArray[rightIndex++];
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        if (l == r)
            return;

        int m = (l + r) / 2;

        // divding arrays into subarrays
        sort(arr, l, m);
        sort(arr, m + 1, r);

        // Call mergeSort from here
        merge(arr, l, m, r);
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