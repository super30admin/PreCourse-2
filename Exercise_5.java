// Time Complexity : O(n log n) on average, O(n^2) in worst case (if pivot is always min or max)
// Space Complexity : O(h), where h is the height of the stack (log n in average case, n in worst case)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Initially had to carefully manage the stack boundaries (low and high) and ensure partition boundaries are valid.

// Your code here along with comments explaining your approach
// We use a manual stack to simulate recursion. The stack stores low and high indices.
// We then use the partition function to divide the array around a pivot and push subarray indices back onto the stack.
class IterativeQuickSort {

    void swap(int arr[], int i, int j) {
        // Swapping without using extra variable
        if (i != j) {
            arr[i] = arr[i] ^ arr[j];
            arr[j] = arr[i] ^ arr[j];
            arr[i] = arr[i] ^ arr[j];
        }
    }

    int partition(int arr[], int low, int high) {
        int pivot = arr[high]; // choose the last element as pivot
        int i = low - 1; // index of smaller element

        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j); // move smaller element to left
            }
        }
        swap(arr, i + 1, high); // place pivot in the correct location
        return i + 1;
    }

    void QuickSort(int arr[], int l, int h) {
        // Create a stack for storing start and end indices
        int[] stack = new int[h - l + 1];

        // initialize top of stack
        int top = -1;

        // push initial values of l and h to stack
        stack[++top] = l;
        stack[++top] = h;

        // Keep popping while stack is not empty
        while (top >= 0) {
            // Pop h and l
            h = stack[top--];
            l = stack[top--];

            // Partitioning index
            int p = partition(arr, l, h);

            // If elements on left side of pivot, push left subarray
            if (p - 1 > l) {
                stack[++top] = l;
                stack[++top] = p - 1;
            }

            // If elements on right side of pivot, push right subarray
            if (p + 1 < h) {
                stack[++top] = p + 1;
                stack[++top] = h;
            }
        }
    }

    void printArr(int arr[], int n) {
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String args[]) {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}
