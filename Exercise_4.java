// Time Complexity : O(nlogn)
// Space Complexity : O(n)
class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // Your code here
        int l1 = m - l + 1;
        int l2 = r - m;
        // arrays to store elements
        int[] a1 = new int[l1];
        int[] a2 = new int[l2];
        for (int i = 0; i < l1; i++)
            a1[i] = arr[l + i];
        for (int i = 0; i < l2; i++)
            a2[i] = arr[m + i + 1];
        int i = 0, j = 0, k = l;

        // Comparing each elements in first and second array and copying them into
        // original array
        while (i < l1 && j < l2) {
            if (a1[i] <= a2[j]) {
                arr[k] = a1[i];
                i++;
            } else {
                arr[k] = a2[j];
                j++;
            }
            k++;
        }
        // copying remaining elements in first array
        while (i < l1) {
            arr[k] = a1[i];
            i++;
            k++;
        }
        // copying remaining elements in second array
        while (j < l2) {
            arr[k] = a2[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        // Write your code here
        // Call mergeSort from here
        if (r > l) {
            // finding the middle point
            int m = (l + r) / 2;
            // sorting the first half of array
            sort(arr, l, m);
            // sorting the second half of array
            sort(arr, m + 1, r);
            // merging the two halves
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