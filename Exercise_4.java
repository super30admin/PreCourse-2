class Exercise_4 {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int[] left, int[] right) {
        int i = 0, j = 0, k = 0;
        int leftRemaining = left.length;
        int rightRemaining = right.length;
        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                arr[k] = left[i];
                i++;
                leftRemaining--;
            } else {
                arr[k] = right[j];
                j++;
                rightRemaining--;
            }
            k++;
        }

        if (leftRemaining >= 0) {
            addRemaining(arr, left, k, leftRemaining);
        } else {
            addRemaining(arr, right, k, rightRemaining);
        }
    }

    void addRemaining(int[] arr, int[] refArr, int indexArrStart, int remainingRefArrElements) {
        while (remainingRefArrElements > 0) {
            arr[indexArrStart] = refArr[refArr.length - remainingRefArrElements];
            remainingRefArrElements--;
            indexArrStart++;
        }

    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        // Write your code here
        // Call mergeSort from here
        if (r < 2) {
            return;
        }
        int midIndex = (l + r) / 2;
        int leftArr[] = new int[midIndex];
        int rightArr[] = new int[arr.length - midIndex];

        for (int i = 0; i < midIndex; i++) {
            leftArr[i] = arr[i];
        }

        for (int j = midIndex; j <= r; j++) {
            rightArr[j - midIndex] = arr[j];
        }
        sort(leftArr, 0, leftArr.length - 1);
        sort(rightArr, 0, rightArr.length - 1);

        merge(arr, leftArr, rightArr);
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