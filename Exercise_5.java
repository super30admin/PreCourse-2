//Time compexity is O(Nlog N)
import java.lang.reflect.Array;
import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        int sum = arr[i] + arr[j];
        arr[i] = sum - arr[i];
        arr[j] = sum - arr[j];
    }

    /*
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int l, int h) {
        // Compare elements and swap.
        int pivot = arr[h];

        int i = l - 1;
        for (int j = l; j <= h - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }

        }
        i++;
        swap(arr, i, h);
        return i;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        Stack<int[]> s = new Stack<>();

        int[] ar = new int[] { l, h };
        s.push(ar);
        while (!s.isEmpty()) {
            int[] a = s.pop();
            int lower = a[0];
            int higher = a[1];
            if (lower <= higher) {
                int x = partition(arr, lower, higher);
                int[] b = new int[] { lower, x - 1 };
                int[] c = new int[] { x + 1, higher };
                s.push(b);
                s.push(c);

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
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}