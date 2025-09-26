// Time Complexity :O ( n log n)
// Space Complexity : O (log n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : I am still not sure from this works, i googled a lot and did it but i am unsure of the logic

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /*
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int l, int h) {
        // Actual logic where elements are swapped according to pivot happens in this
        // function
        int pivot = arr[l];
        int left = l - 1;
        int high = h + 1;
        while (left < high) {
            do {
                left++;
            } while (arr[left] < pivot);
            do {
                high--;
            } while (arr[high] > pivot);
            if (left < high) {
                swap(arr, left, high);
            }
        }
        swap(arr, l, high);
        return high;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        int[] stack = new int[h - l + 1];
        int top = -1;
        stack[++top] = l;
        stack[++top] = h;
        while (top >= 0) {
            h = stack[top--];
            l = stack[top--];
            int pivot = partition(arr, l, h);
            if (pivot - 1 > l) {
                stack[++top] = l;
                stack[++top] = pivot - 1;
            }
            if (pivot + 1 < h) {
                stack[++top] = pivot + 1;
                stack[++top] = h;
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