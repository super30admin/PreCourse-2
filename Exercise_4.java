class Exercise_4 {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // This function gets an array parameter argument with its initial index, end
        // index and respective mid value.
        // Your code here
        // Find sizes of two subarrays to be merged
        // Time complexity is O(n) and space is also O(n)
        /**
         * Logic is we get sizes two halved arrays and their respective index range.
         * We are creating subArrays based on that, provided mid value, begin and end
         * index and we add elements into them respectively.
         * next logic we are sorting two sorted arrays by comparing smallest element and
         * moving respective pointer, if any array has remaining elements then we add
         * those as well,
         *
         *
         */
        int sizeofArrayL = m - l + 1;
        int sizeofArrayR = r - m;

        int ArrayL[] = new int[sizeofArrayL];
        int ArrayR[] = new int[sizeofArrayL];

        for (int idx1 = 0; idx1 < sizeofArrayL; ++idx1)
            ArrayL[idx1] = arr[l + idx1];
        for (int idx2 = 0; idx2 < sizeofArrayR; ++idx2)
            ArrayR[idx2] = arr[m + 1 + idx2];

        int ArrayLIdx = 0, ArrayRIdx = 0;

        int k = l;
        while (ArrayLIdx < sizeofArrayL && ArrayRIdx < sizeofArrayR) {
            if (ArrayL[ArrayLIdx] <= ArrayR[ArrayRIdx]) {
                arr[k] = ArrayL[ArrayLIdx++];

            } else {
                arr[k] = ArrayR[ArrayRIdx++];
            }
            k++;
        }

        while (ArrayLIdx < sizeofArrayL) {
            arr[k++] = ArrayL[ArrayLIdx++];

        }

        while (ArrayRIdx < sizeofArrayR) {
            arr[k++] = ArrayR[ArrayRIdx++];
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        // Write your code here
        // Call mergeSort from here
        /**
         * Here we are checking if beginning index is smaller than end index, then get
         * mid so that we can pass recursively into sort function the 2 divided arrays
         * with help of mid.
         * and then we * call the merge function, to merge them once they are sorted.
         * Merge function is where most of the heavy lifting is done.
         */
        if (l < r) {
            int mid = (l + r) / 2;

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

        Exercise_4 ob = new Exercise_4();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}