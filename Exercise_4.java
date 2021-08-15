class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // calculating the number of elements in both arrays
        int numEls1 = m - l + 1;
        int numEls2 = r - m;

        // creating new arrays using the number of elements
        int[] ar1 = new int[numEls1];
        int[] ar2 = new int[numEls2];

        // populating the arrays with the ranges enabling the split
        for (int i = 0; i < numEls1; i++) {
            ar1[i] = arr[l + i];
        }

        for (int j = 0; j < numEls2; j++) {
            ar2[j] = arr[m + 1 + j];
        }

        // comparing and copying or so called merging into the main array

        int i = 0;
        int j = 0;
        int k = l;

        while (i < numEls1 && j < numEls2) {
            if (ar1[i] <= ar2[j]) {
                arr[k] = ar1[i];
                i++;
            } else {
                arr[k] = ar2[j];
                j++;
            }
            k++;
        }

        while (i < numEls1) {
            arr[k] = ar1[i];
            i++;
            k++;
        }
        while (j < numEls2) {
            arr[k] = ar2[j];
            j++;
            k++;
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
        int arr[] = { 12, 11, 13, 5, 6, 7 };

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}