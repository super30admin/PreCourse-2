import java.util.Stack;

//TC : O(nlogn)
//SC - Worst case : O(n)
//SC - Avg case : O(logn)

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable

        if (i != j) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }

    }

    /*
     * This function is same in both iterative and recursive
     */
    int partition(int arr[], int l, int h) {
        // Compare elements and swap.
        int pivot = arr[h];
        int pIndex = l;
        for (int i = l; i < h; i++) {
            if (arr[i] <= pivot) {
                swap(arr, i, pIndex);
                pIndex++;
            }
        }
        swap(arr, pIndex, h);
        return pIndex;

    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        Stack<int[]> stack = new Stack<>();
        int start = 0;
        int end = arr.length - 1;
        stack.push(new int[] { start, end });

        // loop till stack is empty
        while (!stack.empty()) {

            start = stack.peek()[0];
            end = stack.peek()[1];
            stack.pop();
            int pivot = partition(arr, start, end);
            if (pivot - 1 > start) {
                stack.push(new int[] { start, pivot - 1 });
            }

            if (pivot + 1 < end) {
                stack.push(new int[] { pivot + 1, end });
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