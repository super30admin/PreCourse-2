// Time: O(n log n) average, O(n^2) worst; Space: O(n) explicit range stack

class IterativeQuickSort {
    private void swap(int arr[], int i, int j) {
        // XOR swap avoids a temporary variable; the same index is a no-op.
        if (i != j) {
            arr[i] ^= arr[j];
            arr[j] ^= arr[i];
            arr[i] ^= arr[j];
        }
    }

    int partition(int arr[], int l, int h) {
        int pivot = arr[h];
        int boundary = l - 1;
        for (int current = l; current < h; current++) {
            if (arr[current] <= pivot) {
                swap(arr, ++boundary, current);
            }
        }
        swap(arr, boundary + 1, h);
        return boundary + 1;
    }

    // Store low/high pairs in an array-backed stack to avoid recursion.
    void QuickSort(int arr[], int l, int h) {
        if (l >= h) {
            return;
        }

        int[] ranges = new int[arr.length * 2];
        int top = 0;
        ranges[top++] = l;
        ranges[top++] = h;
        while (top > 0) {
            int high = ranges[--top];
            int low = ranges[--top];
            int pivotIndex = partition(arr, low, high);
            if (low < pivotIndex - 1) {
                ranges[top++] = low;
                ranges[top++] = pivotIndex - 1;
            }
            if (pivotIndex + 1 < high) {
                ranges[top++] = pivotIndex + 1;
                ranges[top++] = high;
            }
        }
    }

    void printArr(int arr[], int n) {
        for (int i = 0; i < n; ++i) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String args[]) {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = {4, 3, 5, 2, 1, 3, 2, 3};
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}
