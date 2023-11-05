// time complexity is O(log n) and space complexity is O(1)
class BinarySearch {
    // Returns index of x if it is present in arr[l..r], else returns -1
    binarySearch(arr, l, r, x) {
        if (r >= l) {
            const mid = l + Math.floor((r - l) / 2);

            // If the element is present at the middle itself
            if (arr[mid] === x) return mid;

            // If the element is in the left subarray
            if (arr[mid] > x) return this.binarySearch(arr, l, mid - 1, x);

            // If the element is in the right subarray
            return this.binarySearch(arr, mid + 1, r, x);
        }

        // If the element is not present in the array
        return -1;
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
