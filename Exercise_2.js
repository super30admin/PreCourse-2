// Time: O(n log n) average, O(n^2) worst; Space: O(log n) average recursion

class QuickSort {
    swap(arr, i, j) {
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }

    // Lomuto partition: move values <= pivot to its left.
    partition(arr, low, high) {
        const pivot = arr[high];
        let boundary = low - 1;
        for (let current = low; current < high; current++) {
            if (arr[current] <= pivot) {
                this.swap(arr, ++boundary, current);
            }
        }
        this.swap(arr, boundary + 1, high);
        return boundary + 1;
    }

    // Sort arr[low..high] in place.
    sort(arr, low, high) {
        if (low < high) {
            const pivotIndex = this.partition(arr, low, high);
            this.sort(arr, low, pivotIndex - 1);
            this.sort(arr, pivotIndex + 1, high);
        }
    }

    printArray(arr) {
        console.log(arr.join(" "));
    }
}

const arr = [10, 7, 8, 9, 1, 5];
const ob = new QuickSort();
ob.sort(arr, 0, arr.length - 1);
console.log("Sorted array");
ob.printArray(arr);
