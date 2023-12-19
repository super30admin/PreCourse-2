import java.util.Stack;
// TC: Best Case: O(N log N); Worst Case: O(N*N)
class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
        if (i != j) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int low, int high)
    {
        int pivot = arr[high];
        for (int i = low; i < high; i++) {
            if (arr[i] < pivot) {
                swap(arr, i, low++);
            }
        }
        swap(arr, high, low);
        return low;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int low, int high)
    {
        Stack<Integer> stack = new Stack<>();
        int pivot = partition(arr, low, high);
        stack.push(pivot);
        while (!stack.isEmpty()) {
            int currPivot = stack.pop();
            if (low < currPivot - 1) {
                pivot = partition(arr, low, currPivot - 1);
                stack.push(pivot);
            }
            if (currPivot + 1 < high) {
                pivot = partition(arr, currPivot + 1, high);
                stack.push(pivot);
            }
            high = currPivot - 1;
            low = currPivot + 1;
        }
    }

    // A utility function to print contents of arr
    void printArr(int arr[], int n)
    {
        int i;
        for (i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
    }

    // Driver code to test above
    public static void main(String args[])
    {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}