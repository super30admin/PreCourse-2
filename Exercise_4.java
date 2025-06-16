// Time Complexity : O(nlogn)
// Space Complexity : O(n)
class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        int s1 = m - l + 1;
        int s2 = r - m;
        // Temporary arrays
        int L[] = new int[s1];
        int R[] = new int[s2];
        for (int i = 0; i < s1; i++) {
            L[i] = arr[l + i];
        }
        for (int j = 0; j < s2; j++) {
            R[j] = arr[m + 1 + j];
        }
        int i = 0, j = 0;
        int k = l;
        while (i < s1 && j < s2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        // copying remaining elements
        while (i < s1) {
            arr[k] = L[i];
            i++;
            k++;
        }
        while (j < s2) {
            arr[k] = R[j];
            j++;
            k++;
        }

    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {

        if (l < r) {
            int mid = (l + r) / 2;
            // sorting first and second half arrays
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
            // Merging sorted half arrays
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