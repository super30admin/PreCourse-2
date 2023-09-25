import java.util.ArrayDeque;
import java.util.Deque;

/**
 * TC: O(n log n) <br>
 * SC: O(log n) due to auxiliary stack space
 */
class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable
        arr[i] ^= arr[j];
        arr[j] ^= arr[i];
        arr[i] ^= arr[j];
    }

    /*
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int low, int high) {
        // Compare elements and swap.
        int pivotIndex = high;
        int pivot = arr[high];
        int l = low;
        int r = high;
        while (l <= r) {
            /**
             * LHS <= pivot
             */
            while (l <= high && arr[l] <= pivot) {
                l++;
            }
            /**
             * RHS > pivot
             */
            while (low <= r && arr[r] > pivot) {
                r--;
            }
            /**
             * if within bounds
             */
            if (l < r) {
                /**
                 * might end up swapping the pivot, so keep track of the pivot
                 */
                if (l == pivotIndex) {
                    pivotIndex = r;
                } else if (r == pivotIndex) {
                    pivotIndex = l;
                }
                swap(arr, l, r);
            }
        }
        /**
         * r == partition index i.e. correct position of the pivot
         * swap the pivot with r
         */
        /**
         * check mandatory as:
         * if pivotIndex == r
         * it results into 0 (when swapping w/o a third variable)
         */
        if (pivotIndex != r) {
            swap(arr, pivotIndex, r);
        }
        return r;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Try using Stack Data Structure to remove recursion.
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(l);
        stack.push(h);

        while (!stack.isEmpty()) {
            h = stack.pop();
            l = stack.pop();

            int partition = partition(arr, l, h);

            // NOTE: if(l >= r) => out of bounds case of recursive implementation
            // check if (l < r)
            if (partition + 1 < h) {
                // sort(arr, partition + 1, high);
                stack.push(partition + 1);
                stack.push(h);
            }

            // NOTE: if(l >= r) => out of bounds case of recursive implementation
            // check if (l < r)
            if (l < partition - 1) {
                // sort(arr, low, partition - 1);
                stack.push(l);
                stack.push(partition - 1);
            }
        }
    }

    // A utility function to print contents of arr
    void printArr(int arr[], int n) {
        int i;
        for (i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
    }

    // Driver code to test above
    public static void main(String args[]) {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}