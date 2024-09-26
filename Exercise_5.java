import java.util.*;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;

    }

    /*
     * This function is same in both iterative and recursive
     */
    int partition(int arr[], int l, int h) {
        // Compare elements and swap.
        int left = l - 1;
        int right = h;
        int pivot = arr[h];
        while (true) {
            while (arr[++left] < pivot && left < right)
                ;
            while (arr[--right] > pivot && right > 0)
                ;
            if (left <= right)
                swap(arr, left, right);
            else
                break;
        }
        swap(arr, left, h);
        return left;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(l);
        stack.push(h);
        while (!stack.isEmpty()) {
            int end = stack.pop();
            int start = stack.pop();
            int partionIndex = partition(arr, start, end);
            if (partionIndex - 1 > start) {
                stack.push(start);
                stack.push(partionIndex - 1);
            }
            if (partionIndex + 1 < end) {
                stack.push(partionIndex + 1);
                stack.push(end);
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