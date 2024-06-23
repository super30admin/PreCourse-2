// Time Complexity: O(n log n) for sorting an array of length n
// Space Complexity: O(log n) for the temporary arrays used during merging

class IterativeQuickSort {

    // Swap elements at index i and j without using extra variable
    void swap(int arr[], int i, int j) {
        if (i != j) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    }

    // Partition function similar to the one in recursive version
    int partition(int arr[], int l, int h) {
        int pivot = arr[h];
        int i = (l - 1); // index of smaller element
        for (int j = l; j <= h - 1; j++) {
            // If current element is smaller than or equal to pivot
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j); // swap arr[i] and arr[j]
            }
        }
        swap(arr, i + 1, h);
        return (i + 1);
    }

    // Iterative QuickSort function
    void QuickSort(int arr[], int l, int h) {
        // Create an auxiliary stack
        int[] stack = new int[h - l + 1];

        // initialize top of stack
        int top = -1;

        // push initial values of l and h to stack
        stack[++top] = l;
        stack[++top] = h;

        // Keep popping from stack while it is not empty
        while (top >= 0) {
            // Pop h and l
            h = stack[top--];
            l = stack[top--];

            // Set pivot element at its correct position in sorted array
            int p = partition(arr, l, h);

            // If there are elements on left side of pivot, then push left side to stack
            if (p - 1 > l) {
                stack[++top] = l;
                stack[++top] = p - 1;
            }

            // If there are elements on right side of pivot, then push right side to stack
            if (p + 1 < h) {
                stack[++top] = p + 1;
                stack[++top] = h;
            }
        }
    }

    // Utility function to print array
    void printArr(int arr[], int n) {
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver code to test above
    public static void main(String args[]) {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}
