// Time Complexity :O(nlogn) where n is no. of elements
// Space Complexity :O(h) where h is no of elements in stack at a time 
// Did this code successfully run on Leetcode :NA
// Any problem you faced while coding this :in partition method, first I was using two pointers but that 
//didn't work and how to use stack was kind of tricky

import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        return;
        // Try swapping without extra variable
    }

    class Range {// making new range class to store in stack
        int x;// start range
        int y;// end range

        Range(int X, int Y) {
            x = X;
            y = Y;
        }

        int getX() {
            return x;
        }// getter methods for both properties

        int getY() {
            return y;
        }
    }

    /*
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int l, int h) {
        int pivot = arr[h];// making last element the pivot
        int lowptr = l;// starting a pointer from low
        for (int i = l; i <= h - 1; i++) {// swapping lowPtr with pivot if element at j is smaller than pivot
            if (arr[i] <= pivot) {
                swap(arr, lowptr, i);
                lowptr++;
            }
        } // at last , the right location of pivot is found after swapping
        swap(arr, lowptr, h);
        return lowptr;// returning the position of pivot
        // Write code here for Partition and Swap
        // Write code here for Partition and Swap
        // Compare elements and swap.
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        Stack<Range> st = new Stack<>();

        st.push(new Range(l, h));
        while (!st.isEmpty()) {
            int x = st.peek().getX();
            int y = st.peek().getY();
            st.pop();
            int pivot = partition(arr, x, y);
            if (x < pivot - 1) {
                st.push(new Range(x, pivot - 1));
            }
            if (pivot + 1 < y) {
                st.push(new Range(pivot + 1, y));
            }
        }
        // Try using Stack Data Structure to remove recursion.
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
