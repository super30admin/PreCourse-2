// Time Complexity :O(nlogn) where n is no. of elements
// Space Complexity :O(h) where h is no of elements in stack at a time of recursion
// Did this code successfully run on Leetcode :NA
// Any problem you faced while coding this :in partition method, first I was using two pointers but that 
//didn't work and how to use stack was kind of tricky
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
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        // arr[i] = arr[i] + arr[j];// storing arr[i]+arr[j] in arr[i]
        // arr[j] = arr[i] - arr[j];// storing arr[i]'s value (to be swapped) in arr[j]
        // by subtract arr[j] from
        // // arr[i]
        // arr[i] = arr[i] - arr[j];// as arr[j] has the swapped, we'll get required
        // arr[i] value by subtracting
        // arr[j] from arr[i]
        return;
        // Your code here
    }

    int partition(int arr[], int low, int high) {
        int pivot = arr[high];// making last element the pivot
        int lowptr = low;// starting a pointer from low
        for (int i = low; i <= high - 1; i++) {// swapping lowPtr with pivot if element at j is smaller than pivot
            if (arr[i] <= pivot) {
                swap(arr, lowptr, i);
                lowptr++;
            }
        } // at last , the right location of pivot is found after swapping
        swap(arr, lowptr, high);
        return lowptr;// returning the position of pivot
        // Write code here for Partition and Swap
    }

    /*
     * The main function that implements QuickSort()
     * arr[] --> Array to be sorted,
     * low --> Starting index,
     * high --> Ending index
     */
    void sort(int arr[], int low, int high) {
        if (low >= high)// if pointers intersect, we stop/return
            return;
        int ptr = partition(arr, low, high);// we get the index of pivot which is placed according to its
        // sorted version
        sort(arr, low, ptr - 1);// we sort left part of the pivot
        sort(arr, ptr + 1, high);// we sort right part of the array
        // Recursively sort elements before
        // partition and after partition
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
        QuickSort ob1 = new QuickSort();
        int arr1[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob1.sort(arr1, 0, arr1.length - 1);
        printArray(arr1);
    }
}
