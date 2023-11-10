// Time Complexity : O(nlogn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : 
// Any problem you faced while coding this : Yes, I have to see youtube video to understand the algorithm how algorithm works.

import java.util.Arrays;

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

        // swapping will be done here
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high) {
        // take last element as a pivot
        int pivot = arr[high];
        // left pointer will be 1 less than low because here we are using do while loop
        // so it will increase by one.
        int i = low - 1;
        // right pointer will be start from high.
        int j = high;
        // if left pointer crosses rigth pointer it means that there is no element on
        // left side that is greater than pivot and same as there is no element on the
        // right side that is less than pivot
        while (i < j) {

            // here we check first element that is less than pivot from right side.
            do {
                j--;
            } while (arr[j] >= pivot);
            // here we check first element that is greater than pivot from left side.

            do {

                i++;
            } while (arr[i] < pivot);
            // once we find element that is greater than pivot from left side and less than
            // pivot from ride side we swap them.
            if (i < j) {
                swap(arr, i, j);
            }

        }

        // if loops break then we find right position for the pivot element. and we put
        // pivot on the right position.
        swap(arr, i, high);
        // return the position of the pivot element.
        return i;
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
        // here we divide the array until left pointer and right pointer cross each
        // other
        if (low < high) {
            // find the pivot element's position
            int j = partition(arr, low, high);
            // here by every recursion we put pivot in its original position and divide two
            // array by pivot and sort them.
            sort(arr, low, j - 1);
            sort(arr, j + 1, high);
        }
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
        // int k = ob.partition(arr, 0, n - 1);

        // System.out.println("sorted array" + k);
        printArray(arr);
    }
}
