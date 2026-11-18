// Time: O(n log n); Space: O(n)

class MergeSort {
    // Merge the already sorted ranges arr[l..m] and arr[m+1..r].
    void merge(int arr[], int l, int m, int r) {
        int[] merged = new int[r - l + 1];
        int left = l;
        int right = m + 1;
        int out = 0;

        // Taking from the left on ties keeps the sort stable.
        while (left <= m && right <= r) {
            merged[out++] = arr[left] <= arr[right] ? arr[left++] : arr[right++];
        }
        while (left <= m) {
            merged[out++] = arr[left++];
        }
        while (right <= r) {
            merged[out++] = arr[right++];
        }
        System.arraycopy(merged, 0, arr, l, merged.length);
    }

    void sort(int arr[], int l, int r) {
        if (l < r) {
            int middle = l + (r - l) / 2;
            sort(arr, l, middle);
            sort(arr, middle + 1, r);
            merge(arr, l, middle, r);
        }
    }

    static void printArray(int arr[]) {
        for (int value : arr) {
            System.out.print(value + " ");
        }
        System.out.println();
    }

    public static void main(String args[]) {
        int arr[] = {12, 11, 13, 5, 6, 7};
        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}
