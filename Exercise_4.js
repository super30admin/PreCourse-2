// Time Complexity: O(n log n)
// Space Complexity: O(n)
class MergeSort {
	// Merges two subarrays of arr[].
	// First subarray is arr[left..mid]
	// Second subarray is arr[mid+1..right]
	merge(arr, left, mid, right) {
		const leftSubarraySize = mid - left + 1;
		const rightSubarraySize = right - mid;

		// create temp arrays to hold the two subarrays
		const leftTempArray = new Array(leftSubarraySize);
		const rightTempArray = new Array(rightSubarraySize);

		// populate temp arrays
		for (let i = 0; i < leftSubarraySize; i++) {
			leftTempArray[i] = arr[left + i];
		}
		for (let j = 0; j < rightSubarraySize; j++) {
			rightTempArray[j] = arr[mid + 1 + j];
		}

		// merge the temp arrays into the original array
		let i = 0; // start of the left subarray
		let j = 0; // start of the right subarray
		let k = left; // start of the merged array

		while (i < leftSubarraySize && j < rightSubarraySize) {
			if (leftTempArray[i] <= rightTempArray[j]) {
				arr[k] = leftTempArray[i];
				i++;
			} else {
				arr[k] = rightTempArray[j];
				j++;
			}
			k++;
		}

		// copy any remaining elements from the left and right temporary array
		while (i < leftSubarraySize) {
			arr[k] = leftTempArray[i];
			i++;
			k++;
		}

		while (j < rightSubarraySize) {
			arr[k] = rightTempArray[j];
			j++;
			k++;
		}
	}

	sort(arr, left, right) {
		if (left < right) {
			const mid = left + Math.floor((right - left) / 2);

			// sort the first and second halves
			this.sort(arr, left, mid);
			this.sort(arr, mid + 1, right);

			// merge the sorted halves
			this.merge(arr, left, mid, right);
		}
	}

	/* A utility function to print array of size n */
	printArray(arr) {
		let n = arr.length;
		for (let i = 0; i < n; ++i) console.log(arr[i] + " ");
		console.log();
	}
}
// Driver method
let arr = [12, 11, 13, 5, 6, 7];
console.log("Given Array");
let ob = new MergeSort();
ob.printArray(arr);
ob.sort(arr, 0, arr.length - 1);
console.log("\nSorted array");
ob.printArray(arr);
