class IterativeQuickSort {

    // time complexity: O(1)
    // space complexity: O(1)
    swap(arr, i, j) {
    //Try swapping without extra variable
        if (i !== j) { // To avoid swapping the same element
            arr[i] = arr[i] ^ arr[j];
            arr[j] = arr[i] ^ arr[j];
            arr[i] = arr[i] ^ arr[j];
        }

    }

    /* This function is same in both iterative and
           recursive*/
    // time complexity: O(n)
    // space complexity: O(1)
    partition(arr, l, h) {
    //Compare elements and swap.
        let pivot = arr[h];
        let i = (l - 1);
        for (let j = l; j <= h - 1; j++) {
            // If current element is smaller than or equal to pivot
            if (arr[j] <= pivot) {
                i++; // increment index of smaller element
                this.swap(arr, i, j);
            }
        }
        this.swap(arr, i+1, h);
        return i+1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    // time complexity: O(n log n)
    // space complexity: O(log n)
    QuickSort(arr, l, h) {
    //Try using Stack Data Structure to remove recursion.
        // Create an auxiliary stack
        let stack = new Array(h - l + 1);

        // initialize top of stack
        let top = -1;

        // push initial values of l and h to stack
        stack[++top] = l;
        stack[++top] = h;

        // Keep popping from stack while is not empty
        while (top >= 0) {
            // Pop h and l
            h = stack[top--];
            l = stack[top--];

            // Set pivot element at its correct position in sorted array
            let p = this.partition(arr, l, h);

            // If there are elements on left side of pivot, then push left side to stack
            if (p - 1 > l) {
                stack[++top] = l;
                stack[++top] = p - 1;
            }

            // If there are elements on right side of pivot, then push right side to stack
            if (p + 1 < h) {
                stack[++top] = p + 1;
                stack[++top] = h;
            }
        }

    }

    // A utility function to print contents of arr
    // time complexity: O(n)
    // space complexity: O(1)
    printArr(arr, n) {
        let i;
        for (i = 0; i < n; ++i)
            console.log(arr[i] + " ");
    }
}

  // Driver code to test above
let ob = new IterativeQuickSort();
let arr = [4, 3, 5, 2, 1, 3, 2, 3];
[1, 2, 2, 3, 3, 3, 4, 5]
ob.QuickSort(arr, 0, arr.length - 1);
ob.printArr(arr, arr.length);
