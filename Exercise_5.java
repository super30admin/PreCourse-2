import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Your code here
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high) {
        // Write code here for Partition and Swap
        int j = low;
        for (int i = low; i < high; i++) {
            if (arr[i] <= arr[high]) {
                swap(arr, i, j);
                j++;
            }
        }
        swap(arr, high, j);
        return j;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(l);
        stack.push(h);

        int high = 0, low = 0;

        while (!stack.isEmpty()) {
            high = stack.pop();
            low = stack.pop();

            if (low <= high) {
                int partitionIndex = partition(arr, low, high);

                stack.push(partitionIndex + 1);
                stack.push(high);

                stack.push(low);
                stack.push(partitionIndex - 1);
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