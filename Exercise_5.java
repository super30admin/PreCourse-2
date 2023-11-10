
//time o(n*n) where n is the length of the array
//space o(1) 
import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable
        if (i == j)
            return;
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }

    /*
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int l, int h) {
        // Compare elements and swap.

        int pivot = arr[h];
        int partition = l - 1;
        for (int i = l; i <= h; i++) {
            if (arr[i] <= pivot)
                swap(arr, i, ++partition);
        }
        return partition;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Try using Stack Data Structure to remove recursion.
        Stack stack = new Stack<>();
        stack.push(l);
        stack.push(h);
        while (stack.empty() == false) {
            h = (int) stack.pop();
            l = (int) stack.pop();
            int partition = partition(arr, l, h);
            if (partition - 1 > l) { // left
                stack.push(l);
                stack.push(partition - 1);
            }
            if (partition + 1 < h) { // right
                stack.push(partition + 1);
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
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}