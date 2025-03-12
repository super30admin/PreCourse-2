class IterativeQuickSort {
    void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /* This function is same in both iterative and 
       recursive*/
    int partition(int[] arr, int l, int h) {
        int i = l - 1;
        //Compare elements and swap.
        for (int j = l; j <= h - 1; j++) {
            i++;
            swap(arr, i, j);
        }
        swap(arr, l, h);
        return l;
    }

    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int[] arr, int l, int h) {
        //Stack Data Structure to remove recursion.
        int stack[] = new int[h - l + 1];

        //initialize top of stack
        int top = -1;

        // push initial values to the stack
        stack[++top] = l;
        stack[++top] = h;

        //pop all elements until empty
        while (top >= 0) {
            h = stack[top--];
            l = stack[top--];

            int pivot = partition(arr, l, h);

            // If there are elements on left side of pivot,
            // then push left side to stack
            if (pivot - 1 > l) {
                stack[++top] = l;
                stack[++top] = pivot - 1;
            }

            // If there are elements on right side of pivot,
            // then push right side to stack
            if (pivot + 1 < h) {
                stack[++top] = pivot + 1;
                stack[++top] = h;
            }
        }
    }

    // A utility function to print contents of arr 
    void printArr(int[] arr, int n) {
        int i;
        for (i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
    }

    // Driver code to test above 
    public static void main(String[] args) {
        IterativeQuickSort ob = new IterativeQuickSort();
        int[] arr = {4, 3, 5, 2, 1, 3, 2, 3};
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}

/**
 * Time Complexity: O(n log n)
 * Space Complexity: O(n)
 */