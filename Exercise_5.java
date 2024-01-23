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

    int partition(int arr[], int l, int h) {
        int pivot = arr[h];
        int i = (l - 1);

        for (int j = l; j < h; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, h);
        return i + 1;
    }

    void QuickSort(int arr[], int l, int h) {
        // Create an auxiliary stack
        Stack<Integer> stack = new Stack<>();

        // Push initial values of l and h to the stack
        stack.push(l);
        stack.push(h);

        // Keep popping from the stack until it is empty
        while (!stack.isEmpty()) {
            // Pop h and l
            h = stack.pop();
            l = stack.pop();

            // Set pivot element at its correct position in sorted array
            int p = partition(arr, l, h);

            // If there are elements on the left side of the pivot, push them to the stack
            if (p - 1 > l) {
                stack.push(l);
                stack.push(p - 1);
            }

            // If there are elements on the right side of the pivot, push them to the stack
            if (p + 1 < h) {
                stack.push(p + 1);
                stack.push(h);
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
        int arr[] = {4, 3, 5, 2, 1, 3, 2, 3};
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}
