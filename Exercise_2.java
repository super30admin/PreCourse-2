// complexity is O(nlogn) average case and O(n^2) worst case
class QuickSort {
    /*
     * This function takes last element as pivot,
     * places the pivot element at its correct
     * position in sorted array, and places all
     * smaller (smaller than pivot) to left of
     * pivot and all greater elements to right
     * of pivot
     */
    void swap(int arr[], int i, int j) {
        // Your code here
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    }

    // complexity is O(n)
    int partition(int arr[], int low, int high) {
        // Write code here for Partition and Swap
        int pivot = arr[high];
        int new_pivot = low;

        // swapping the values as many times as the count of numbers less than the last number of the subarray

        for (int i = low; i <= high-1; i++) {
            if (arr[i] <= pivot) {
                this.swap(arr, i, new_pivot);
                new_pivot++;
            }
        }
        this.swap(arr, new_pivot, high);
        return new_pivot;
    }

    /*
     * The main function that implements QuickSort()
     * arr[] --> Array to be sorted,
     * low --> Starting index,
     * high --> Ending index
     */
    // complexity is O(log n) avg and O(n) worse case * complexity of partition function
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
        if(low >= high){
            return;
        }
        int pivot = this.partition(arr, low, high);
        // find the pivot and split apply the same function on either sides of the pivot
        this.sort(arr, low, pivot-1);
        this.sort(arr, pivot+1, high);
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver program
    public static void main(String args[]) {
        // int arr[] = { 10, 7, 8, 9, 1, 5 };
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);

        System.out.println("sorted array");
        printArray(arr);
    }
}
