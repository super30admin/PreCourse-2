// Time Complexity:
//    Average Case: O(n log n)
//    - Partition work per level: O(n) - scans through all elements in current ranges
//    - Number of levels: O(log n) - balanced partitions divide array roughly in half
//    - Total: O(n) x O(log n) = O(n log n)
//    Worst Case: O(n²)
//    - Levels: O(n) instead of O(log n)
//    - Total: O(n) x O(n) = O(n^2)

// Space Complexity
//    Average Case: O(log n) - balanced partitions, stack depth log n
//    Worst Case: O(n) - stack depth can grow to n levels

import java.util.Stack;

class IterativeQuickSort {

  void swap(int arr[], int i, int j) {
    //Try swapping without extra variable

    // handle same index
    if (i == j) {
      return;
    }

    arr[i] = arr[i] + arr[j];
    arr[j] = arr[i] - arr[j];
    arr[i] = arr[i] - arr[j];
  }

  /* This function is same in both iterative and
     recursive*/
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

  // Sorts arr[l..h] using iterative QuickSort
  void QuickSort(int arr[], int l, int h) {
    //Try using Stack Data Structure to remove recursion.

    // Input validation
    if (arr == null || arr.length <= 1) {
      return;
    }
    if (l < 0 || h >= arr.length || l > h) {
      return;
    }

    Stack<Integer> leftStack = new Stack<>();
    Stack<Integer> rightStack = new Stack<>();

    // push initial range
    leftStack.push(l);
    rightStack.push(h);

    while (!leftStack.isEmpty()) {
      int left = leftStack.pop();
      int right = rightStack.pop();

      if (left < right) {  // process if more than 1 element
        int pivotIndex = partition(arr, left, right);

        // push left subarray (if it needs sorting)
        if (left < pivotIndex - 1) {
          leftStack.push(left);
          rightStack.push(pivotIndex - 1);
        }

        // push right subarray (if it needs sorting)
        if (pivotIndex + 1 < right) {
          leftStack.push(pivotIndex + 1);
          rightStack.push(right);
        }
      }
    }
  }

  // A utility function to print contents of arr
  void printArr(int arr[], int n) {
    int i;
    for (i = 0; i < n; ++i) {
      System.out.print(arr[i] + " ");
    }
  }

  // Driver code to test above
  public static void main(String args[]) {
    IterativeQuickSort ob = new IterativeQuickSort();
    int arr[] = {4, 3, 5, 2, 1, 3, 2, 3};
    ob.QuickSort(arr, 0, arr.length - 1);
    ob.printArr(arr, arr.length);
  }
}