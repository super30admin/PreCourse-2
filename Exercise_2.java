class QuickSort
{
    /* This function swaps two elements in the array */
    void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /* This function takes last element as pivot, places the pivot element at its correct
       position in sorted array, and places all smaller elements to left of pivot and
       all greater elements to right of pivot */
    int partition(int arr[], int low, int high)
    {
        int pivot = arr[high];
        int pi = low;

        for (int i = low; i < high; i++) {
            if (arr[i] <= pivot) {
                swap(arr, pi, i);
                pi++;
            }
        }
        swap(arr, pi, high);
        return pi;
    }

    /* The main function that implements QuickSort */
    void sort(int arr[], int low, int high)
    {
        if (low < high) {
            int pi = partition(arr, low, high);
            sort(arr, low, pi - 1);
            sort(arr, pi + 1, high);
        }
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver program
    public static void main(String args[])
    {
        int arr[] = {10, 7, 8, 9, 1, 5};
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);

        System.out.println("Sorted array");
        printArray(arr);
    }
}
