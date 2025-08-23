// Time Complexity: O(n log n)
//    Height of tree = log n levels
//    Work per level = O(n)
//    Total work = O(n) × O(log n) = O(n log n)

// Space Complexity: O(n)
//  Recursion Stack:
//  - Space per call = constant
//  - Maximum simultaneous calls = log n (depth)
//  - Total stack space = constant x log n = O(log n)
//  Temporary Arrays:
//  - Space per merge = up to n elements
//  - Temporary arrays are created/destroyed, not stacked
//  - Maximum temp space at any moment = O(n)
//
//  Total = Recursion Stack + Temporary Arrays = O(log n) + O(n) = O(n)

// Any problem you faced while coding this : I always had trouble processing recursion in my head

class MergeSort {

  // Merges two subarrays of arr[].
  // First subarray is arr[l..m]
  // Second subarray is arr[m+1..r]
  void merge(int arr[], int l, int m, int r) {
    // sizes
    int leftSize = m - l + 1;
    int rightSize = r - (m + 1) + 1;

    // temp arrays
    int[] leftArr = new int[leftSize];
    int[] rightArr = new int[rightSize];
    // copy data
    for (int i = 0; i < leftSize; i++) {
      leftArr[i] = arr[l + i];
    }
    for (int i = 0; i < rightSize; i++) {
      rightArr[i] = arr[m + 1 + i];
    }

    // merge
    int i = 0, j = 0, k = l;

    while (i < leftSize && j < rightSize) {
      if (leftArr[i] <= rightArr[j]) {
        arr[k] = leftArr[i];
        i++;
      } else {
        arr[k] = rightArr[j];
        j++;
      }
      k++;
    }

    // handle remaining elements
    while (i < leftSize) {
      arr[k] = leftArr[i];
      i++;
      k++;
    }

    while (j < rightSize) {
      arr[k] = rightArr[j];
      j++;
      k++;
    }
  }

  // Main function that sorts arr[l..r] using
  // merge()
  void sort(int arr[], int l, int r) {
    if (arr == null || arr.length <= 1) {
      return; // nothing to sort
    }

    // base case
    if (l >= r) {
      return;
    }

    // find middle point
    int mid = l + (r - l) / 2;

    // recursively sort left half
    sort(arr, l, mid);

    // recursively sort right half
    sort(arr, mid + 1, r);

    // merge the two sorted halves
    merge(arr, l, mid, r);
  }

  /* A utility function to print array of size n */
  static void printArray(int arr[]) {
    int n = arr.length;
    for (int i = 0; i < n; ++i) {
      System.out.print(arr[i] + " ");
    }
    System.out.println();
  }

  // Driver method
  public static void main(String args[]) {
    int arr[] = {12, 11, 13, 5, 6, 7};

    System.out.println("Given Array");
    printArray(arr);

    MergeSort ob = new MergeSort();
    ob.sort(arr, 0, arr.length - 1);

    System.out.println("\nSorted array");
    printArray(arr);
  }
}