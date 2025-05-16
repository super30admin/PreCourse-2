import java.util.Stack;

class IterativeQuickSort {

    void swap(int arr[], int i, int j) {
        // Swapping without extra variable using XOR
        if (i != j) {
            arr[i] = arr[i] ^ arr[j];
            arr[j] = arr[i] ^ arr[j];
            arr[i] = arr[i] ^ arr[j];
        }
    }

    /* Partition function similar to recursive version */
    int partition(int arr[], int l, int h) {
        int pivot = arr[h];
        int i = l - 1;

        for (int j = l; j <= h - 1; j++) {
            // If current element is smaller than or equal to pivot
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, h);
        return i + 1;
    }

    // Iterative QuickSort using Stack
    void QuickSort(int arr[], int l, int h) {
        Stack<Integer> stack = new Stack<>();

        // Push initial values of l and h
        stack.push(l);
        stack.push(h);

        // Keep popping while stack is not empty
        while (!stack.isEmpty()) {
            h = stack.pop();
            l = stack.pop();

            // Partition the array and get pivot index
            int p = partition(arr, l, h);

            // If there are elements on the left of pivot, push left side to stack
            if (p - 1 > l) {
                stack.push(l);
                stack.push(p - 1);
            }

            // If there are elements on the right of pivot, push right side to stack
            if (p + 1 < h) {
                stack.push(p + 1);
                stack.push(h);
            }
        }
    }

    // A utility function to print contents of arr
    void printArr(int arr[], int n) {
        for (int i = 0; i < n; ++i)
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
