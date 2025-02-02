class QuickSort {

    // Swap function to exchange values at indices i and j
    swap(arr, i, j) {
        let temp = arr[i]; // Temporarily store the value at index i
        arr[i] = arr[j]; // Assign the value at index j to index i
        arr[j] = temp; // Assign the temporarily stored value to index j
    }

    // Partition function: Chooses the last element as pivot, places it at its correct position, 
    // and arranges smaller elements to the left and greater elements to the right.
    partition(arr, low, high) {
        let pivot = arr[high]; // Choose the last element as pivot
        let i = low - 1; // Set the initial position for the smaller element

        // Traverse the array from low to high-1
        for (let j = low; j < high; j++) {
            // If the current element is smaller than or equal to the pivot
            if (arr[j] <= pivot) {
                i++; // Move the smaller element pointer to the right
                this.swap(arr, i, j); // Swap the current element with the element at i
            }
        }

        // Place the pivot in the correct position
        this.swap(arr, i + 1, high);
        return i + 1; // Return the index of the pivot
    }

    // Main quicksort function that sorts the array
    sort(arr, low, high) {
        if (low < high) {
            let pi = this.partition(arr, low, high); // Find the pivot index

            // Recursively sort elements before and after the partition
            this.sort(arr, low, pi - 1);
            this.sort(arr, pi + 1, high);
        }
    }

    // Utility function to print the array
    printArray(arr) {
        let n = arr.length;
        for (let i = 0; i < n; ++i) {
            console.log(arr[i] + " ");
        }
        console.log();
    }
}

// Driver program
let arr = [10, 7, 8, 9, 1, 5];
let n = arr.length;
let ob = new QuickSort();
ob.sort(arr, 0, n - 1); // Sort the array
console.log("Sorted array");
ob.printArray(arr); // Print the sorted array
