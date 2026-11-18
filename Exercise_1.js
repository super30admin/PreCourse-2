// Time: O(log n); Space: O(1)

class BinarySearch {
    // Return the index of x in sorted arr[l..r], or -1 when it is absent.
    binarySearch(arr, l, r, x) {
        while (l <= r) {
            const mid = l + Math.floor((r - l) / 2);
            if (arr[mid] === x) {
                return mid;
            }
            if (arr[mid] < x) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return -1;
    }
}

const ob = new BinarySearch();
const arr = [2, 3, 4, 10, 40];
const result = ob.binarySearch(arr, 0, arr.length - 1, 10);
if (result === -1) {
    console.log("Element not present");
} else {
    console.log("Element found at index " + result);
}
