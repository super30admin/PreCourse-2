//Time Complexity: O(nlogn)
//Space Complexity: O(n)

class MergeSort {

  //Merging two sorted arrays, but rather two sorted arr use two part of the arr, left to mid and mid+1 to right
  void merge(int arr[], int l, int m, int r) {
    int left = l;
    int right = m + 1;
    //to traverse new arr
    int idx = 0;

    //Initialize newArr to store the value the sorted values
    int newArr[] = new int[r - l + 1];

    //Traverse the array until left and right cross their end
    while (left <= m && right <= r) {
      //Check if value of left it less than values of right, if yes then copy it to newArr, later increment idx and left else do the same with right value
      if (arr[left] <= arr[right]) {
        newArr[idx] = arr[left];
        idx++;
        left++;
      } else {
        newArr[idx] = arr[right];
        idx++;
        right++;
      }
    }

    //if the length of arr given is odd, the above traversal stops after the shorter section crosses its end so to get the last element of the other section we use below loops
    while (left <= m) {
      newArr[idx] = arr[left];
      idx++;
      left++;
    }

    while (right <= r) {
      newArr[idx] = arr[right];
      idx++;
      right++;
    }

    //copy the values from newArr to give array
    left = l;
    idx = 0;

    while (left <= r) {
      arr[left] = newArr[idx];
      left++;
      idx++;
    }
  }

  //Sort array by dividing the arr into smaller arrays and sorting them recursively
  void sort(int arr[], int l, int r) {
    //return if only one element is present as it always sorted
    if (l >= r) {
      return;
    }

    //Calculate mid value to dive the arr into two parts
    int mid = (l + r) / 2;

    // Call the sort the left section
    sort(arr, l, mid);
    // Call to sort the right section
    sort(arr, mid + 1, r);
    //Merge both left and right sorted sections
    merge(arr, l, mid, r);
  }

  /* A utility function to print array of size n */
  static void printArray(int arr[]) {
    int n = arr.length;
    for (int i = 0; i < n; ++i) System.out.print(arr[i] + " ");
    System.out.println();
  }

  // Driver method
  public static void main(String args[]) {
    int arr[] = { 12, 11, 13, 5, 6, 7 };

    System.out.println("Given Array");
    printArray(arr);

    MergeSort ob = new MergeSort();
    ob.sort(arr, 0, arr.length - 1);

    System.out.println("\nSorted array");
    printArray(arr);
  }
}
