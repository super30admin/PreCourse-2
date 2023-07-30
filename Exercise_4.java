class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int left[], int right[]) {
        // Your code here
        int leftIndex = 0;
        int rightIndex = 0;
        int mainIndex = 0;
        while (leftIndex <= left.length - 1 && rightIndex <= right.length - 1) {
            if (left[leftIndex] <= right[rightIndex]) {
                arr[mainIndex] = left[leftIndex];
                leftIndex++;
            } else {
                arr[mainIndex] = right[rightIndex];
                rightIndex++;
            }
            mainIndex++;
        }
        while (leftIndex <= left.length - 1) {
            arr[mainIndex] = left[leftIndex];
            leftIndex++;
            mainIndex++;
        }
        while (rightIndex <= right.length - 1) {
            arr[mainIndex] = right[rightIndex];
            rightIndex++;
            mainIndex++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[]) {
        // Write your code here
        // Call mergeSort from here
        if (arr.length < 2)
            return;

        int mid = arr.length / 2;
        int[] left = new int[mid];
        int[] right = new int[arr.length - mid];

        for (int i = 0; i <= mid - 1; i++) {
            left[i] = arr[i];
        }
        for (int i = mid; i <= arr.length - 1; i++) {
            right[i - mid] = arr[i];
        }

        sort(left);
        sort(right);

        merge(arr, left, right);
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
        ob.sort(arr);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}