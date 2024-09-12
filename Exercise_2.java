class QuickSort
{

    /**
     * swap values of arr[i] and arr[j] in array
     * @param arr
     * @param i
     * @param j
     */
    //time complexity :o(1)
    //Space complexity:o(1)
    void swap(int arr[],int i,int j){
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }

    /**
     * This function takes last element as pivot, places the pivot element at its correct
     * position in sorted array, and places all smaller (smaller than pivot) to left of
     * pivot and all greater elements to right of pivot
     * @param arr input arr of integers
     * @param low lowest index in array
     * @param high highest index in array
     * @return returns the index of the element which is put at its correct place
     */
    int partition(int arr[], int low, int high) {
        int pivot = arr[high];
        int i = low;

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                swap( arr, i, j );
                i++;
            }
        }
        swap( arr, i, high );
        return i;
    }

    /**
     * The main function that implements QuickSort()
     * @param arr Array to be sorted,
     * @param low Starting index,
     * @param high Ending index
     */
    /*Time complexity:o(n log n) in average case, where n is array size
                       o(n)^2  in worst case, when array is already sorted
       Space complexity :o(1) As we are using constant space here.
     */
    void sort(int arr[], int low, int high)
    {
            // Recursively sort elements before
            // partition and after partition
        if(low<high) {
              int idx=partition(arr,low,high);
              sort(arr,low,idx-1);
              sort(arr,idx+1,high);
        }
    }

    /* A utility function to print array of size n */
    //Time complexity:o(n)
    //space complexity:o(1)
    static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i]+" ");
        System.out.println();
    }

    // Driver program
    public static void main(String args[])
    {
        int arr[] = {10, 7, 8, 9, 1, 5};
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n-1);

        System.out.println("sorted array");
        printArray(arr);
    }
}
