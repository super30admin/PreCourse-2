//Time Complexity: O(nlogn)
//Space Complexity: O(n)

import java.util.Stack;

class IterativeQuickSort {

  //Store the value of i in temp and then update the value of i, with value of j then update value of j with temp
  void swap(int arr[], int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }

  //To make sure all the values less than pivot are to left and right consist of all the element greater than pivot
  int partition(int arr[], int low, int high) {
    int i = low;
    int j = high;

    //Traverse the until lo is less than hi
    while (i < j) {
      //find the value less than pivot from left
      while (i < high && arr[i] <= arr[low]) i++;
      //find the value greater than pivot from right
      while (j > low && arr[j] >= arr[low]) j--;

      //if the above loops stop that means their are incorrectly positioned values so we swap them
      if (i < j) {
        swap(arr, i, j);
      }
    }

    //swap the pivot to its correct position
    swap(arr, low, j);
    return j;
  }

  // Sorts arr[l..h] using iterative QuickSort
  void QuickSort(int arr[], int low, int high) {
    if (low >= high) return;

    // Each element on the stack is a {low, high} pair:
    Stack<int[]> stack = new Stack<>();
    stack.push(new int[] { low, high });

    while (!stack.isEmpty()) {
      // Pop a range to sort
      int[] range = stack.pop();
      int l = range[0], h = range[1];

      // find the index of pivot element
      int pivot = partition(arr, l, h);

      // If there’s a left segment, push its bounds to stack
      if (l < pivot - 1) {
        stack.push(new int[] { l, pivot - 1 });
      }
      // If there’s a right segment, push its bounds to stack
      if (pivot + 1 < h) {
        stack.push(new int[] { pivot + 1, h });
      }
    }
  }

  // A utility function to print contents of arr
  void printArr(int arr[], int n) {
    int i;
    for (i = 0; i < n; ++i) System.out.print(arr[i] + " ");
  }

  // Driver code to test above
  public static void main(String args[]) {
    IterativeQuickSort ob = new IterativeQuickSort();
    int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
    ob.QuickSort(arr, 0, arr.length - 1);
    ob.printArr(arr, arr.length);
  }
}
