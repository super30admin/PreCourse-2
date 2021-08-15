class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /*
     * This function is same in both iterative and recursive
     */
    int partition(int arr[], int l, int h) {
        int pivot = arr[h];
        int j = l - 1;
        for (int i = l; i < h; i++) {
            if (arr[i] < pivot) {
                j++;
                swap(arr, i, j);
            }

        }
        swap(arr, j + 1, h);
        return j + 1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
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