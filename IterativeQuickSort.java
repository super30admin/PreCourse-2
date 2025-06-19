/*
 * Iterative QuickSort using Hoare's partition scheme (pivot = last element)
 *
 * Time Complexity:
 *   - Best Case:    O(n log n)
 *   - Average Case: O(n log n)
 *   - Worst Case:   O(n^2)   
 *
 * Space Complexity:
 *   - Auxiliary Stack Space: O(log n) average, O(n) worst (due to stack)
 */

import java.util.Stack;

class IterativeQuickSort {

    // Swaps two elements in the array
    void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // Partition using Hoare’s scheme with pivot as the last element
    int partition(int arr[], int l, int h) {
        int pivot = arr[h];
        int i = l;
        int j = h;

        while (true) {
            while (i <= h && arr[i] < pivot) i++;
            while (j >= l && arr[j] > pivot) j--;

            if (i >= j) return i;

            swap(arr, i, j);
            i++;
            j--;
        }
    }

    // Iterative QuickSort using stack
    void QuickSort(int arr[], int low, int high) {
        Stack<int[]> stack = new Stack<>();

        // Push the initial range
        stack.push(new int[]{low, high});

        while (!stack.isEmpty()) {
            int[] state = stack.pop();
            int l = state[0], h = state[1];

            if (l < h) {
                int p = partition(arr, l, h);

                // Push right subarray
                if (p < h)
                    stack.push(new int[]{p, h});

                // Push left subarray
                if (l < p - 1)
                    stack.push(new int[]{l, p - 1});
            }
        }
    }

    // Utility to print the array
    void printArr(int arr[], int n) {
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver code
    public static void main(String args[]) {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = {4, 3, 5, 2, 1, 3, 2, 3};
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}
