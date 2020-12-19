import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        if(i==j)
            return;
        
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }

    int partition(int arr[], int l, int h) {
        int pivot = arr[h];
        int start_index = l;
        for (int i = l; i < h; i++) {
            if (arr[i] < pivot) {
                swap(arr, i, start_index++);
            }
        }
        swap(arr, start_index, h);
        return start_index;
    }

    // Time complexity : O(nlogn)
    // Space complexity : O(n)
    void QuickSort(int arr[], int l, int h) {
        Stack<int[]> stack = new Stack<>();
        stack.add(new int[] { l, h });
        while (!stack.isEmpty()) {
            int t[] = stack.pop();
            int low = t[0];
            int high = t[1];
            if (low < high) {
                int partition = partition(arr, low, high);
                stack.add(new int[] { low, partition - 1 });
                stack.add(new int[] { partition + 1, high });
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