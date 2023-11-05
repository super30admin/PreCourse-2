// time complexity is O(logn) and space complexity is O(n)

class QuickSort {
    /* This function takes last element as pivot,
       places the pivot element at its correct
       position in the sorted array, and places all
       smaller (smaller than pivot) to the left of
       pivot and all greater elements to the right
       of the pivot */

    swap(arr, i, j) {
        let temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    partition(arr, low, high) {
        let pivot = arr[high];
        let i = low - 1;

        for (let j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                this.swap(arr, i, j);
            }
        }

        this.swap(arr, i + 1, high);
        return i + 1;
    }

    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
    sort(arr, low, high) {
        if (low < high) {
            let pi = this.partition(arr, low, high);

            this.sort(arr, low, pi - 1);
            this.sort(arr, pi + 1, high);
        }
    }

    /* A utility function to print the array */
    printArray(arr) {
        let n = arr.length;
        for (let i = 0; i < n; ++i)
            console.log(arr[i] + " ");
        console.log();
    }
}

// Driver program
let arr = [10, 7, 8, 9, 1, 5];
let n = arr.length;
let ob = new QuickSort();
ob.sort(arr, 0, n - 1);
console.log("Sorted array:");
ob.printArray(arr);
