// Time Complexity : O(n log n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes (https://leetcode.com/problems/sort-an-array/)
// Any problem you faced while coding this : no

import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        //Try swapping without extra variable
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) {
        int pivotValue = arr[h];
        int left = (l - 1);

        for (int i = l; i <= h; i++) {
            if (arr[i] < pivotValue) {
                swap(arr, ++left, i);
            }
        }
        left++;
        swap(arr, left, h);
        return left;
    }

    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) {
        if (h - l + 1 <= 1) {
            return;
        }
        Stack<Integer> st = new Stack<>();
        st.push(l);
        st.push(h);

        while (!st.isEmpty()) {
            h = st.pop();
            l = st.pop();
            int p = partition(arr, l, h);
            if (p - 1 > l) {
                st.push(l);
                st.push(p - 1);
            }
            if (p + 1 < h) {
                st.push(p + 1);
                st.push(h);
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
        int arr[] = {-1243, 4, 30, 5, 2, 1, 3, 2, 3, 100, 1243};
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
} 