/*Time Complexity : O(n log n)
 Space Complexity : O(1), no additional cost

 Your code here along with comments explaining your approach:
 Divide the input array by finding pivot element. Move all elements less than pivot to left
 and all elements greater than pivot to the right of pivot index. Once pivot is positioned correctly,
 sort the left and the right sub array recursively.
*/

class QuickSort {
    /* This function takes last element as pivot,
       places the pivot element at its correct
       position in sorted array, and places all
       smaller (smaller than pivot) to left of
       pivot and all greater elements to right
       of pivot */
    void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high) {
        int pivotIndex = high;
        for (int i = low; i < high; i++) {
            if (arr[i] < arr[pivotIndex]) {
                swap(arr, low, i);
                low += 1;
            }
        }
        swap(arr, pivotIndex, low);
        pivotIndex = low;
        return pivotIndex;
    }

    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
    void sort(int arr[], int low, int high) {
        if (low < high) {
            int pivotIndex = partition(arr, low, high);
            sort(arr, low, pivotIndex - 1);
            sort(arr, pivotIndex + 1, high);
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
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);

        System.out.println("sorted array");
        printArray(arr);
    }
} 
