// Time Complexity : Not sure
// Space Complexity : Not sure
// Did this code successfully run on Leetcode : 
// Any problem you faced while coding this : Referred some documention and videos and coded but did not understood properly and not sure how this time complexity?

import java.util.Stack;

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
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int l, int h) {
        // Compare elements and swap.
        int pivot = arr[h];
        int i = l - 1;

        for (int j = l; j < h; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }

        }

        swap(arr, i + 1, h);
        return i + 1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Declare stack
        Stack<Integer> stack = new Stack<>();
        // Push the low and high values
        stack.push(l);
        stack.push(h);

        while (!stack.isEmpty()) {
            // Pop from the stack and get the partion index and iteratively repeat it on the
            // sub arrays
            int high = stack.pop();
            int low = stack.pop();
            if (low < high) {
                int pi = partition(arr, low, high);

                stack.push(low);
                stack.push(pi - 1);

                stack.push(pi + 1);
                stack.push(high);
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