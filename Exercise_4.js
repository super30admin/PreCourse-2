class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    merge(arr, l, m, r) {
        // Find the sizes of two subarrays to be merged
        let n1 = m - l + 1;
        let n2 = r - m;

        // Create temporary arrays
        let left = new Array(n1);
        let right = new Array(n2);

        // Copy data to temporary arrays left[] and right[]
        for (let i = 0; i < n1; i++) {
            left[i] = arr[l + i];
        }
        for (let j = 0; j < n2; j++) {
            right[j] = arr[m + 1 + j];
        }

        // Merge the temporary arrays back into arr[l..r]
        let i = 0; // Initial index of first subarray
        let j = 0; // Initial index of second subarray
        let k = l; // Initial index of merged subarray

        while (i < n1 && j < n2) {
            if (left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        // Copy the remaining elements of left[], if any
        while (i < n1) {
            arr[k] = left[i];
            i++;
            k++;
        }

        // Copy the remaining elements of right[], if any
        while (j < n2) {
            arr[k] = right[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using merge()
    sort(arr, l, r) {
        if (l >= r) {
            return; // Base case: single element or no element
        }

        // Find the middle point
        let m = Math.floor((l + r) / 2);

        // Recursively sort the first and second halves
        this.sort(arr, l, m);
        this.sort(arr, m + 1, r);

        // Merge the sorted halves
        this.merge(arr, l, m, r);
    }

    // A utility function to print the array of size n
    static printArray(arr) {
        for (let i = 0; i < arr.length; i++) {
            process.stdout.write(arr[i] + " ");
        }
        console.log();
    }
}

// Driver method
let arr = [12, 11, 13, 5, 6, 7];

console.log("Given Array:");
MergeSort.printArray(arr);

let mergeSort = new MergeSort();
mergeSort.sort(arr, 0, arr.length - 1);

console.log("\nSorted Array:");
MergeSort.printArray(arr);
