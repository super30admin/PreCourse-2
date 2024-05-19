// Time Complexity : O(nlogn)
// Space Complexity : O(log n) due to stack usage
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Yes, took a lot of time to understand what is going on.

import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        if (i != j) { // swapping
            arr[i] =arr[i]+arr[j];
            arr[j] =arr[i]-arr[j];
            arr[i] =arr[i]-arr[j];
        }
   }

    int partition(int arr[], int low, int high) {
        int pivot = arr[high]; // setting the pivot to last element of the array
        int i = low - 1; // starting i from left side, if it starts from 0 then proper swap wont be done as well as check.

        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return i + 1;
    }

    void QuickSort(int arr[], int l, int h) {
        Stack<Integer> stack = new Stack<>();
        stack.push(l); // pushing low to stack
        stack.push(h); // pushing high to stack
        while (!stack.isEmpty()) {
            h = stack.pop();
            l = stack.pop();
            int pivot = partition(arr, l, h); // setting low and high
            if (pivot- 1>l) {
                stack.push(l);
                stack.push(pivot-1);
            }
            if (pivot+1 <h) {
                stack.push(pivot + 1);
                stack.push(h);
            }
        }
    }

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