//Time Complexity: O(n)
//Space Complexity: O(1)

class BinarySearch {

  // Returns index of x if it is present in arr[l.. r], else return -1
  int binarySearch(int arr[], int l, int r, int x) {
    int lo = l;
    int hi = r;

    while (lo <= hi) {
      // Find the value of mid
      int mid = lo + (hi - lo) / 2;

      //Check if arr of mid is required element
      if (arr[mid] == x) {
        return mid;
        //Else if arr of mid is less than x then we move to search on the right side
      } else if (arr[mid] < x) {
        lo = mid + 1;
        //Else i.e arr of mid is greater than x then we move to search of left side which contains values smaller than mid
      } else {
        hi = mid - 1;
      }
    }

    return -1;
  }

  // Driver method to test above
  public static void main(String args[]) {
    BinarySearch ob = new BinarySearch();
    int arr[] = { 2, 3, 4, 10, 40 };
    int n = arr.length;
    int x = 10;
    int result = ob.binarySearch(arr, 0, n - 1, x);
    if (result == -1) System.out.println("Element not present");
    else System.out.println("Element found at index " + result);
  }
}
