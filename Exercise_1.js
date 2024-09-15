class BinarySearch {
     // Returns index of x if it is present in arr[l.. r], else return -1
    function binarySearch(arr, l, r, x) {
​
    }
}
// Driver method to test above
const ob = new BinarySearch();
const arr = [2, 3, 4, 10, 40];
const n = arr.length;
const x = 10;
const result = ob.binarySearch(arr, 0, n - 1, x);
if (result === -1)
    console.log("Element not present");
else
    console.log("Element found at index " + result);
