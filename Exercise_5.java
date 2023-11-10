
// T.C : O(nlogn)
// S.C : O(1)
import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable
        if (arr[i] == arr[j])
            return;
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];

    }

    /*
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int low, int high) {
        // Compare elements and swap.
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j <= high; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i, low);
        return i;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Try using Stack Data Structure to remove recursion.
        Stack<Integer> s = new Stack();
        s.push(l);
        s.push(h);
        while (!s.isEmpty()) {
            h = s.pop();
            l = s.pop();
            int pivot = partition(arr, l, h);
            if ((pivot - 1) > l) {
                s.push(l);
                s.push(pivot - 1);
            }
            if ((pivot + 1) < h) {
                s.push(pivot + 1);
                s.push(h);
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