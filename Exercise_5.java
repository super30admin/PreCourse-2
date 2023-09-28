//time complexity- O(nlog(n))
//space complexity- O(n)
class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /*
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int l, int h) {
        // Compare elements and swap.
        int pivot = arr[h];
        int i = l - 1, j = l;
        while (j < h) {
            if (arr[j] < pivot) {
                swap(arr, i + 1, j);
                i++;
            }
            j++;
        }
        i += 1;
        swap(arr, i, h);
        return i;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Try using Stack Data Structure to remove recursion.
        if (h - l + 1 <= 1)
            return;
        int stack[] = new int[h - l + 1];
        int top = -1;
        stack[++top] = l;
        stack[++top] = h;
        while (top >= 0) {
            int high = stack[top--];
            int low = stack[top--];
            int mid = partition(arr, low, high);
            if (mid - 1 > low) {
                stack[++top] = low;
                stack[++top] = mid - 1;
            }
            if (mid + 1 < high) {
                stack[++top] = mid + 1;
                stack[++top] = high;
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