//time complexity - O(6log6)
//space complexity - O(6)


class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // Your code here
        int leftlen = m - l + 1;
        int rightlen = r - m;
        int[] lefthalf = new int[leftlen];
        int[] righthalf = new int[rightlen];

        for (int i = 0; i < leftlen; i++) {
            lefthalf[i] = arr[l + i];
        }
        for (int j = 0; j < rightlen; j++) {
            righthalf[j] = arr[m + 1 + j];
        }

        int i = 0, j = 0;

        int k = l;
        while (i < rightlen && j < leftlen) {
            if (lefthalf[i] <= righthalf[j]) {
                arr[k] = lefthalf[i];
                i++;
            } else {
                arr[k] = righthalf[j];
                j++;

            }
            k++;
        }

        while (i < leftlen) {
            arr[k] = lefthalf[i];
            i++;
            k++;
        }
        while (j < rightlen) {
            arr[k] = righthalf[j];
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