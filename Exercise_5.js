class IterativeQuickSort {

    // Swap function without using an extra variable
    swap(arr, i, j) {
        arr[i] = arr[i] + arr[j];  // Add arr[i] to arr[j]
        arr[j] = arr[i] - arr[j];  // Subtract arr[j] from arr[i] to get arr[i]
        arr[i] = arr[i] - arr[j];  // Subtract arr[i] from arr[j] to get arr[j]
    }

    // Partition function to partition the array around a pivot
    partition(arr, l, h) {
        let pivot = arr[h];  // Pivot is the last element
        let i = l - 1;  // Index for the smaller element

        for (let j = l; j <= h - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                this.swap(arr, i, j);  // Swap if the element is smaller than the pivot
            }
        }
        this.swap(arr, i + 1, h);  // Place the pivot in its correct position
        return i + 1;  // Return the pivot index
    }

    // Iterative QuickSort function using a stack
    QuickSort(arr, l, h) {
        // Create an empty stack to simulate recursive calls
        let stack = [];

        // Push initial values of l and h to the stack
        stack.push(l);
        stack.push(h);

        // Continue sorting while the stack is not empty
        while (stack.length > 0) {
            h = stack.pop();  // Pop high index
            l = stack.pop();  // Pop low index

            // Partition the array and get the pivot index
            let pivot = this.partition(arr, l, h);

            // If there are elements to the left of the pivot, push the left subarray indices
            if (pivot - 1 > l) {
                stack.push(l);
                stack.push(pivot - 1);
            }

            // If there are elements to the right of the pivot, push the right subarray indices
            if (pivot + 1 < h) {
                stack.push(pivot + 1);
                stack.push(h);
            }
        }
    }

    // Utility function to print the array
    printArr(arr) {
        console.log(arr.join(" "));
    }

    // Driver code to test the above
    static main() {
        let ob = new IterativeQuickSort();
        let arr = [4, 3, 5, 2, 1, 3, 2, 3];
        ob.QuickSort(arr, 0, arr.length - 1);  // Sort the array
        ob.printArr(arr);  // Print the sorted array
    }
}

// Call the main function
IterativeQuickSort.main();
