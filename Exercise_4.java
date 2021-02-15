// Time Complexity : O(nlogn)
// Dividing the array takes O(1) time
// merging the sorted array takes O(n) time 
// recursively applying sort algorithm on the halved arrays take O(logn) time. 

// Space Complexity : O(n)

class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // size of the two array halves
        int leftArrSize = m - l + 1, rightArrSize = r - m;

        // creating the tem array to hold the elements from two halves before sorting
        int[] leftArr = new int[leftArrSize], rightArr = new int[rightArrSize];

        // inserting elements to the two temp arrays
        for (int i = 0; i < leftArrSize; i++) {
            leftArr[i] = arr[l + i];
        }

        for (int j = 0; j < rightArrSize; j++) {
            rightArr[j] = arr[m + j + 1];
        }

        int left = 0, right = 0, currIndex = l;

        // traversing both the halves, and inserting the elements in sorted order to the
        // original array
        while (left < leftArrSize && right < rightArrSize) {
            if (leftArr[left] <= rightArr[right]) {
                arr[currIndex] = leftArr[left++];
            } else {
                arr[currIndex] = rightArr[right++];
            }
            currIndex++;
        }

        // inserting the elements that may have left over in the left half
        while (left < leftArrSize)
            arr[currIndex++] = leftArr[left++];

        // inserting the elements that may have left over in the right half
        while (right < rightArrSize)
            arr[currIndex++] = rightArr[right++];
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        if (l < r) {
            int m = l + (r - l) / 2;
            sort(arr, l, m);
            sort(arr, m + 1, r);

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