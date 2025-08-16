// Time Complexity: O(log n)
// Space Complexity: O(1)
class BinarySearch {
	// Returns index of x if it is present in arr[l.. r], else return -1
	binarySearch(arr, left, right, target) {
		if (!arr || arr.length === 0) return -1;

		if (left === right) {
			return arr[left] === target ? left : -1;
		}
		while (left <= right) {
			let mid = Math.floor((left + right) / 2);

			if (arr[mid] === target) {
				return mid;
			} else if (arr[mid] < target) {
				left = mid + 1;
			} else {
				right = mid - 1;
			}
		}

		return -1;
	}
}
// Driver method to test above
const ob = new BinarySearch();
const arr = [2, 3, 4, 10, 40];
const n = arr.length;
const x = 10;
const result = ob.binarySearch(arr, 0, n - 1, x);
if (result === -1) {
	console.log("Element not present");
} else {
	console.log("Element found at index " + result);
}
