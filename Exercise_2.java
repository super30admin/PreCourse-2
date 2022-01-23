// Time Complexity :
// AVG : [Partition algo O(n)] + 2*Q.S.[n/2] ~~ 0(nLog(n));
// Worst : [Partition algo O(n)] + Q.S(n-1) ~~ O(n^2)
// Space Complexity : If partitioned balanced then O(Log(n)) like Merge sort; but in worst case unbalanced then levels would be equal to N so O(nLog(n))
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : determining complexity and understanding stack tree calls
class QuickSort {
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[], int i, int j) {
        //Your code here
        // System.out.println("Swapping i with j : " + arr[i] + "," + arr[j]);
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // To place the pivot, at its correct position
    int partition(int arr[], int low, int high) {
        //Write code here for Partition and Swap
        int pivot = high;
        int divider = -1;
        int i = 0;
        for (i = 0; i < high; i++) {
            // System.out.println("Checking i with pivot : " + arr[i] + "," + arr[pivot]);
            if (arr[i] <= arr[pivot]) {
                //  divider point to elems less than picot; so increment divider and swap;
                divider++;
                swap(arr, i, divider);
            }
        }
        swap(arr, divider + 1, pivot);
        return divider + 1;
    }

    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) {
        // Recursively sort elements before
        // partition and after partition
        System.out.println("QS low,high " + low + "," + high);
        if (low < high) {
            int pivot = partition(arr, low, high);
            sort(arr, low, pivot - 1);
            sort(arr, pivot + 1, high);
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
        int arr[] = {10, 7, 8, 9, 1, 5};
        System.out.println("original array");
        printArray(arr);
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);

        System.out.println("sorted array");
        printArray(arr);
    }
} 
