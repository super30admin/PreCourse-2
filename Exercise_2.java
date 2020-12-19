class QuickSort {
   
    void swap(int arr[], int i, int j) {
        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }

    int partition(int arr[], int low, int high) {
        int pivot = arr[high];
        int start_index = low;
        for (int i = low; i < high; i++) {
            if (arr[i] < pivot) {
                swap(arr, i, start_index++);
            }
        }
        swap(arr, start_index, high);
        return start_index;
    }

    //Time complexity : O(nlogn)
    //Space Complexity : O(1) (Ignoring function call stack)
    void sort(int arr[], int low, int high) {
        if (low < high) {
            int partition = partition(arr, low, high);
            sort(arr, low, partition - 1);
            sort(arr, partition + 1, high);
        }
    }

    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver program
    public static void main(String args[]) {
        int arr[] = { 1,2,3,9,8,7,6,5,5,5 };
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);

        System.out.println("sorted array");
        printArray(arr);
    }
}
