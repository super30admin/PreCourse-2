class IterativeQuickSort {
    // Swap without using a temporary variable
    swap(arr, i, j) {
        if (i !== j) { 
            arr[i] = arr[i] ^ arr[j];
            arr[j] = arr[i] ^ arr[j];
            arr[i] = arr[i] ^ arr[j];
        }
    }

    // Lomuto partition scheme
    partition(arr, l, h) {
        let pivot = arr[h]; // Last element as pivot
        let i = l - 1; // Pointer for smaller element

        for (let j = l; j < h; j++) {
            if (arr[j] < pivot) {
                i++;
                this.swap(arr, i, j); // Swap smaller element to correct position
            }
        }
        this.swap(arr, i + 1, h); // Move pivot to correct position
        return i + 1;
    }

    // Iterative QuickSort using stack
    QuickSort(arr, l, h) {
        let stack = []; // Stack to simulate recursion

        // Push initial values of l and h
        stack.push(l);
        stack.push(h);

        while (stack.length > 0) {
            // Pop h and l
            h = stack.pop();
            l = stack.pop();

            // Partition index
            let p = this.partition(arr, l, h);

            // Push left subarray to stack if it has more than one element
            if (p - 1 > l) {
                stack.push(l);
                stack.push(p - 1);
            }

            // Push right subarray to stack if it has more than one element
            if (p + 1 < h) {
                stack.push(p + 1);
                stack.push(h);
            }
        }
    }

    // Utility function to print array
    printArr(arr, n) {
        console.log(arr.join(" "));
    }
}

// Driver code
let ob = new IterativeQuickSort();
let arr = [4, 3, 5, 2, 1, 3, 2, 3];
console.log("Given Array:");
ob.printArr(arr, arr.length);

ob.QuickSort(arr, 0, arr.length - 1);

console.log("Sorted Array:");
ob.printArr(arr, arr.length);
