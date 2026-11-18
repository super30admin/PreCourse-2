// Time: O(n log n) average, O(n^2) worst; Space: O(log n) average recursion

class QuickSort {
    private void swap(int arr[], int i, int j) {
        int value = arr[i];
        arr[i] = arr[j];
        arr[j] = value;
    }

    // Lomuto partition: move values <= pivot to its left.
    int partition(int arr[], int low, int high) {
        int pivot = arr[high];
        int boundary = low - 1;
        for (int current = low; current < high; current++) {
            if (arr[current] <= pivot) {
                swap(arr, ++boundary, current);
            }
        }
        swap(arr, boundary + 1, high);
        return boundary + 1;
    }

    // Sort arr[low..high] in place.
    void sort(int arr[], int low, int high) {
        if (low < high) {
            int pivotIndex = partition(arr, low, high);
            sort(arr, low, pivotIndex - 1);
            sort(arr, pivotIndex + 1, high);
        }
    }

    static void printArray(int arr[]) {
        for (int value : arr) {
            System.out.print(value + " ");
        }
        System.out.println();
    }

    public static void main(String args[]) {
        int arr[] = {10, 7, 8, 9, 1, 5};
        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, arr.length - 1);
        System.out.println("Sorted array");
        printArray(arr);
    }
}
