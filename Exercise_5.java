import java.util.Stack;

class IterativeQuickSort {
    // Time Complexity: O(NlogN)  - O(n) to position the pivot and O(logN) called recursively on left and right sub arrays
    // Space Complexity: O(1)
    // Did this code successfully run on Leetcode : Passed 17/21 test cases for this problem = https://leetcode.com/problems/sort-an-array/description/?envType=problem-list-v2&envId=merge-sort
    // Any problem you faced while coding this : Yes, when index i and j were equal the value being inserted was becoming 0. fixed that by not swapping values when i==j

    void swap(int[] arr, int i, int j)
    {
	    //Try swapping without extra variable
        if (i == j) // do not swap if the index is the same
            return;
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int[] arr, int l, int h)
    {
        //Compare elements and swap.
        //Write code here for Partition and Swap
        int pivot = arr[h];
        int i = l - 1; // pointer for tracking smaller elements
        for (int j = l; j < h; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i+1, h); // pivot should be placed immediately after smaller elements,
        // so it is i+1 to ensure smaller elements are placed left
        return i+1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void quickSort(int[] arr, int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[] {l, h});

        while(!stack.isEmpty()) {
            int[] boundary = stack.pop();
            l = boundary[0];
            h = boundary[1];

            if (l < h) {
                int pivotIndex = partition(arr, l, h);
                stack.push(new int[] {l, pivotIndex - 1});
                stack.push(new int[] {pivotIndex + 1, h});
            }
        }
    }

    // A utility function to print contents of arr
    void printArr(int[] arr, int n)
    {
        int i;
        for (i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
    }

    // Driver code to test above
    public static void main(String[] args)
    {
        IterativeQuickSort ob = new IterativeQuickSort();
        int[] arr = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.quickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}