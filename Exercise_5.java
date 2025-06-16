/*
Time Complexity: O(n log n)
Space Complexity: O(n)
*/
class IterativeQuickSort {

    // Swap without using extra variable (if i != j)
    void swap(int arr[], int i, int j) {
        if (i != j) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    }

    // Partition function same as recursive version
    int partition(int arr[], int l, int h) {
        int pivot = arr[h];
        int i = l - 1;

        for (int j = l; j <= h - 1; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, h);
        return i + 1;  // pivot index
    }

    // Iterative QuickSort function
    void QuickSort(int arr[], int l, int h) {
        int size = h - l + 1;
        int[] stack = new int[size];

        int top = -1;

        // Push initial values of l and h to stack
        stack[++top] = l;
        stack[++top] = h;

        // Keep popping while stack is not empty
        while (top >= 0) {
            // Pop h and l
            h = stack[top--];
            l = stack[top--];

            // Partition the array and get pivot index
            int p = partition(arr, l, h);

            // If there are elements on the left side of pivot, push left side to stack
            if (p - 1 > l) {
                stack[++top] = l;
                stack[++top] = p - 1;
            }

            // If there are elements on the right side of pivot, push right side to stack
            if (p + 1 < h) {
                stack[++top] = p + 1;
                stack[++top] = h;
            }
        }
    }

    // Print array function
    void printArr(int arr[], int n) {
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver code to test above
    public static void main(String args[]) {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        System.out.println("Original array:");
        ob.printArr(arr, arr.length);

        ob.QuickSort(arr, 0, arr.length - 1);

        System.out.println("Sorted array:");
        ob.printArr(arr, arr.length);
    }
}
