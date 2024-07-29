class QuickSort {
    // Function to swap two elements in the array
    swap(arr, i, j) {
        let temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // Function to partition the array and return the pivot index
    // time complexity: O(n)
    // space complexity: O(1)
    partition(arr, low, high) {
        let pivot = arr[high]; 
        let i = low - 1; 

        for (let j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                this.swap(arr, i, j);
            }
        }
        this.swap(arr, i + 1, high);
        return i + 1;
    }

    // The main function that implements QuickSort
    // time complexity: O(n log n)
    // space complexity: O(log n)
    sort(arr, low, high) {
        if (low < high) {
            let pi = this.partition(arr, low, high);
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
    }
}

// Driver program
let arr = [10, 7, 8, 9, 1, 5];
let n = arr.length;
let ob = new QuickSort();
console.log("Original array:");
ob.printArray(arr);
ob.sort(arr, 0, n - 1);
console.log("Sorted array:");
ob.printArray(arr);
