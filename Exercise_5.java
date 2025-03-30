/*
Iterative QuickSort Algorithm:
- This implementation uses a stack to simulate the recursive behavior of QuickSort.
- The pivot is chosen as the last element of the array.
- The partition function rearranges the array so that elements smaller than the pivot are on the left, and larger ones are on the right.

Time Complexity:
- Best/Average Case: O(n log n)
- Worst Case: O(n^2) (when the pivot is always the smallest or largest element)

Space Complexity:
- O(log n) in the best/average case (due to stack usage).
- O(n) in the worst case (when recursion depth is maximum).
*/

class IterativeQuickSort {

    // Swap two elements in the array
    void swap(int[] arr, int i, int j) {
        if (i != j) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    }

    // Partition the array and return the pivot index
    int partition(int[] arr, int low, int high) {
        int pivot = arr[high]; // Choose the last element as the pivot
        int i = low - 1; // Pointer for smaller elements

        for (int j = low; j < high; j++) {
            // If the current element is smaller than or equal to the pivot
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j); // Swap the elements
            }
        }

        // Place the pivot in its correct position
        swap(arr, i + 1, high);
        return i + 1; // Return the pivot index
    }

    // Iterative QuickSort function
    void quickSort(int[] arr, int low, int high) {
        // Create a stack to store subarray indices
        int[] stack = new int[high - low + 1];
        int top = -1; // Initialize the stack pointer

        // Push the initial indices of the array onto the stack
        stack[++top] = low;
        stack[++top] = high;

        // Process the stack until it's empty
        while (top >= 0) {
            // Pop the high and low indices
            high = stack[top--];
            low = stack[top--];

            // Partition the array and get the pivot index
            int pivotIndex = partition(arr, low, high);

            // If there are elements on the left of the pivot, push their indices onto the stack
            if (pivotIndex - 1 > low) {
                stack[++top] = low;
                stack[++top] = pivotIndex - 1;
            }

            // If there are elements on the right of the pivot, push their indices onto the stack
            if (pivotIndex + 1 < high) {
                stack[++top] = pivotIndex + 1;
                stack[++top] = high;
            }
        }
    }

    // Utility function to print the array
    void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    // Main method to test the QuickSort implementation
    public static void main(String[] args) {
        IterativeQuickSort sorter = new IterativeQuickSort();
        int[] arr = {4, 3, 5, 2, 1, 3, 2, 3};
        System.out.println("Original Array:");
        sorter.printArray(arr);

        sorter.quickSort(arr, 0, arr.length - 1);

        System.out.println("Sorted Array:");
        sorter.printArray(arr);
    }
}