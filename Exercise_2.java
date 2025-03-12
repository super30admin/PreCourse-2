class QuickSort {
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int[] arr, int low, int high) {
        //pivot
        int pivot = arr[high];
        int i = low - 1;

        // Traverse arr[low..high] and move all smaller
        // elements compared with pivot to the left side. Elements from low to
        // i are smaller after every iteration
        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        //Move pivot after smaller elements and return it's position
        swap(arr, i + 1, high);
        return i + 1;
    }

    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int[] arr, int low, int high) {
        // Recursively sort elements before
        // partition and after partition
        if (low < high) {
            //returns index of pivot
            int pi = partition(arr, low, high);

            //Recursion
            sort(arr, low, pi - 1);
            sort(arr, pi + 1, high);
        }
    }

    /* A utility function to print array of size n */
    static void printArray(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver program 
    public static void main(String[] args) {
        int[] arr = {10, 7, 8, 9, 1, 5};
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);

        System.out.println("sorted array");
        printArray(arr);
    }
}

//Time Complexity: Avg - O(n log n)
/**
 * Even though we always pick the last element as the pivot, on average, the partitioning will split the array fairly evenly. This results in:
 * •	Partitioning each step takes O(n).
 * •	The recursion depth is O(log n) (because we keep dividing the array into two roughly equal halves).
 * •	Total time complexity = O(n log n).
 */

//Space Complexity: O(log n)
/**
 * Since QuickSort uses recursion, the call stack depth depends on the number of times the array is split.
 * •	On average, if partitioning is balanced, the recursion depth is O(log n).
 * •	Each recursive call only uses O(1) extra space (in-place sorting).
 * •	Total space complexity = O(log n) (stack space for recursive calls).
 */
