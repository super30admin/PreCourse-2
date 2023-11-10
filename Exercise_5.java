// Time Complexity : O(n logn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : NA
// Any problem you faced while coding this : None.

import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable
        int curr = arr[i];
        arr[i] = arr[j];
        arr[j] = curr;
    }

    /*
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int l, int h) {
        // Compare elements and swap.
        int pivot = arr[h];

        // index of smaller element
        int i = (l - 1);
        for (int j = l; j <= h - 1; j++) {
            // If current element is smaller than or
            // equal to pivot
            if (arr[j] <= pivot) {
                i++;
                // swap arr[i] and arr[j]
                swap(arr, i, j);
            }
        }

        // swap arr[i+1] and arr[h] (or pivot)
        swap(arr, i + 1, h);

        return i + 1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<Integer>();

        stack.push(l);
        stack.push(h);

        // Keep popping from stack while is not empty
        while (!stack.isEmpty()) {
            // Pop h and l
            h = stack.pop();
            l = stack.pop();

            int p = partition(arr, l, h);

            if (p - 1 > l) {
                stack.add(l);
                stack.add(p - 1);
            }

            if (p + 1 < h) {
                stack.add(p + 1);
                stack.add(h);
            }
            // System.out.println(stack.peek());
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