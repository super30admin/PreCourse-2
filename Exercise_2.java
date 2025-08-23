// Time Complexity :
//    Average case: O(n log n)
//       Time per level = O(n) (always process n elements total)
//       Number of levels = O(log n)
//       Total time = O(n x log n) = elements x levels
//    Worst case: O(n^2) when pivot is always smallest/largest (with unbalanced partitions, recursion goes n levels deep)

// Space Complexity :
//   Average Case: O(log n)
//       - With balanced partitions, recursion goes log n levels deep
//       - Each level stores: array reference, low, high, pivotIdx = constant
//       - Total: constant x log n = O(log n)
//   Worst Case: O(n) - unbalanced partitions goes n levels deep

// Any problem you faced while coding this : no

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
    int pivot = arr[high]; // last element as pivot
    int boundary = low; // track where next small element goes

    for (int i = low; i < high; i++) {
      if (arr[i] <= pivot) {  // when we find element <= pivot
        swap(arr, boundary, i); // place it to the boundary position
        boundary++;             // move boundary pointer
      }
    }

    swap(arr, boundary, high); // place pivot right after all small elements
    return boundary; // return pivot's final position
  }

  /* The main function that implements QuickSort()
    arr[] --> Array to be sorted,
    low  --> Starting index,
    high  --> Ending index */
  void sort(int arr[], int low, int high) {
    // Input validation
      if (arr == null || arr.length <= 1) {
          return;
      }
      if (low < 0 || high >= arr.length || low > high) {
          return;
      }

    // base case
    if (low >= high) {
      return;
    }

    // partition the array
    // after partition, the pivot is in its final correct position
    // so, we exclude the pivot from both recursive calls
    int pivotIdx = partition(arr, low, high);

    // recursively sort left subarray
    sort(arr, low, pivotIdx - 1);

    // recursively sort right subarray
    sort(arr, pivotIdx + 1, high);
  }

  /* A utility function to print array of size n */
  static void printArray(int arr[]) {
    int n = arr.length;
      for (int i = 0; i < n; ++i) {
          System.out.print(arr[i] + " ");
      }
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
