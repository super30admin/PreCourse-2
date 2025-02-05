// Time Complexity : O(n log n) in average and best cases, O(n^2) in worst case (when pivot selection is poor)
// Space Complexity : O(log n) in average case (stack usage for partitioning), O(n) in worst case
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach

import java.util.Stack;

class IterativeQuickSort { 
    // Swaps two elements in the array without using an extra variable
    void swap(int arr[], int i, int j) { 
        if (i != j) {
            arr[i] = arr[i] ^ arr[j];
            arr[j] = arr[i] ^ arr[j];
            arr[i] = arr[i] ^ arr[j];
        }
    } 

    // Partition function (Lomuto partitioning)
    int partition(int arr[], int l, int h) { 
        int pivot = arr[h]; // Choosing the last element as pivot
        int i = l - 1; // Index of smaller element

        for (int j = l; j < h; j++) { 
            // If current element is smaller than or equal to pivot
            if (arr[j] <= pivot) { 
                i++;
                swap(arr, i, j);
            } 
        } 
        swap(arr, i + 1, h); // Swap pivot into correct position
        return i + 1;
    } 

    // Iterative QuickSort using a stack to remove recursion
    void QuickSort(int arr[], int l, int h) { 
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{l, h});

        while (!stack.isEmpty()) {
            int[] range = stack.pop();
            int low = range[0], high = range[1];

            if (low < high) {
                int pivot = partition(arr, low, high);

                // Push left subarray
                if (pivot - 1 > low) {
                    stack.push(new int[]{low, pivot - 1});
                }
                // Push right subarray
                if (pivot + 1 < high) {
                    stack.push(new int[]{pivot + 1, high});
                }
            }
        }
    } 

    // A utility function to print contents of arr 
    void printArr(int arr[], int n) { 
        for (int i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println();
    } 

    // Driver code to test above 
    public static void main(String args[]) { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = {4, 3, 5, 2, 1, 3, 2, 3}; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
}
