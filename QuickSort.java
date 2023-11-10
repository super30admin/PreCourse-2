// Time Complexity :  O(nlogn) for best and avergae case 
//                 :  O(n^2) for worst case ; where n is the no. of elements in the array
// Space Complexity : O(logn) for average case
//                  : O(n) for worst case as there need to made n recursive calls in recursion stack

//Code:

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
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high) {
        // Write code here for Partition and Swap
        int i = low, j = low;
        int pivot = arr[high]; // taking pivot as the element at high index as pivot will reach at its correct
                               // position after partition
        while (i <= high) {
            if (arr[i] <= pivot) { // if arr[i] is smaller than pivot then we need to swap the elements and
                                   // increement their indexes
                swap(arr, i, j);
                i++;
                j++;
            } else {
                i++;
            }
        }
        return (j - 1);
    }

    /*
     * The main function that implements QuickSort()
     * arr[] --> Array to be sorted,
     * low --> Starting index,
     * high --> Ending index
     */
    void sort(int arr[], int low, int high) {
        // Recursively sort elements before
        // partition and after partition
        if (low > high)
            return;

        int pi = partition(arr, low, high);
        sort(arr, low, pi - 1);
        sort(arr, pi + 1, high);
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
        int arr[] = { 10, 7, 8, 9, 1, 5 };
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);

        System.out.println("sorted array");
        printArray(arr);
    }
}
