// Time Complexity : O(log n) because we eliminate half the search space each iteration
// Space Complexity : O(1) only using a constant amount of extra space (variables mid, l, r)
// Any problem you faced while coding this : no

class BinarySearch {

  // Returns index of x if it is present in arr[l.. r], else return -1
  int binarySearch(int arr[], int l, int r, int x) {
    while (l
        <= r) { // keep searching until the boundaries cross, which definitively proves the element isn't there
      int mid = l + (r - l) / 2; // overflow prevention

      if (arr[mid] == x) {
        return mid; // found element
      } else if (arr[mid] < x) {
        l = mid + 1; // exclude mid, search right half
      } else {
        r = mid - 1; // exclude mid, search left half
      }
    }

    return -1; // element not found
  }

  // Driver method to test above
  public static void main(String args[]) {
    BinarySearch ob = new BinarySearch();
    int arr[] = {2, 3, 4, 10, 40};
    int n = arr.length;
    int x = 10;
    int result = ob.binarySearch(arr, 0, n - 1, x);
      if (result == -1) {
          System.out.println("Element not present");
      } else {
          System.out.println("Element found at index " + result);
      }
  }
} 
