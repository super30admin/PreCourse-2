//Time Complexity: O(NlogN)
//Space Complexity: O(1)

class QuickSort {

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
      while (i <= high && arr[i] <= arr[low]) i++;
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

  //Recursively sorting the array using divide and conquer techniques
  void sort(int arr[], int low, int high) {
    // if low > high, which means the array was traverse completely and sorted
    if (low >= high) {
      return;
    }

    //find the index of pivot element
    int pivot = partition(arr, low, high);
    //sort the left section of arr
    sort(arr, low, pivot - 1);
    //sort the right section of arr
    sort(arr, pivot + 1, high);
  }

  /* A utility function to print array of size n */
  static void printArray(int arr[]) {
    int n = arr.length;
    for (int i = 0; i < n; ++i) System.out.print(arr[i] + " ");
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
