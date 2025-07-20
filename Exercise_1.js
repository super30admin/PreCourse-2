class BinarySearch {
  // Returns index of x if it is present in arr[l.. r], else return -1
  binarySearch(arr, l, r, x) {
    if (!arr || arr.length == 0) return -1;

    while (l <= r) {
      const middle = l + Math.floor((r - l) / 2);
      if (x == arr[middle]) {
        return middle;
      } else if (arr[middle] < x) {
        l = middle + 1;
      } else {
        r = middle - 1;
      }
    }

    return -1;
  }
}
// Driver method to test above
const ob = new BinarySearch();
const arr = [2, 3, 4, 10, 40];
const n = arr.length;
const x = 2;
const result = ob.binarySearch(arr, 0, n - 1, x);
if (result === -1) console.log("Element not present");
else console.log("Element found at index " + result);
