import java.util.Stack;

class IterativeQuickSort {

    // Swapping without using an extra variable (using XOR swap)
    void swap(int arr[], int i, int j) {
        if (i != j) { // Avoid zeroing elements if i == j
            arr[i] = arr[i] ^ arr[j];
            arr[j] = arr[i] ^ arr[j];
            arr[i] = arr[i] ^ arr[j];
        }
    }

    // Partition function (Lomuto partition scheme)
    int partition(int arr[], int l, int h) {
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

    // Iterative QuickSort using explicit stack
    void QuickSort(int arr[], int l, int h) {
        // Create stack
        Stack<Integer> stack = new Stack<>();

        // Push initial values of l and h to stack
        stack.push(l);
        stack.push(h);

        // Keep popping until stack is empty
        while (!stack.isEmpty()) {
            h = stack.pop();
            l = stack.pop();

            // Partition the array and get pivot index
            int p = partition(arr, l, h);

            // If elements on the left of pivot, push left side to stack
            if (p - 1 > l) {
                stack.push(l);
                stack.push(p - 1);
            }

            // If elements on the right of pivot, push right side to stack
            if (p + 1 < h) {
                stack.push(p + 1);
                stack.push(h);
            }
        }
    }

    // Utility function to print array
    void printArr(int arr[], int n) {
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver code
    public static void main(String args[]) {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = {4, 3, 5, 2, 1, 3, 2, 3};
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}


//Time complexity : O(n log n)
//Space complexity : O(log n)