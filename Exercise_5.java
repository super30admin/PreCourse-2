import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable
    }

    /*
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int low, int high) {
        int pivot = arr[low];
        int i = low;
        int j = high;

        while (i <= j) {
            while (i <= high && arr[i] <= pivot) {
                i++;
            }
            while (arr[j] > pivot) {
                j--;
            }
            if (i < j) {
                swap(arr, i, j);
            }
        }

        arr[low] = arr[j];
        arr[j] = pivot;

        return j;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        Stack<Integer> stack = new Stack<>();

        // Push initial values of h and l to stack
        stack.push(h);
        stack.push(l);

        // Keep popping from stack while is not empty
        while (!stack.isEmpty()) {
            // Pop l and h
            l = stack.pop();
            h = stack.pop();

            // Set pivot element at its correct position
            // in sorted array
            int p = partition(arr, l, h);

            // If there are elements on left side of pivot,
            // then push left side to stack
            if (p - 1 > l) {
                stack.push(p - 1);
                stack.push(l);
            }

            // If there are elements on right side of pivot,
            // then push right side to stack
            if (p + 1 < h) {
                stack.push(h);
                stack.push(p + 1);
            }
        }
    }

    // A utility function to print contents of arr
    void printArr(int arr[], int n) {
        int i;
        for (i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
    }
}

public class Exercise_5 {
    // Driver code to test above
    public static void main(String args[]) {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}