// Time: O(n log n) average, O(n^2) worst; Space: O(n) explicit range stack

class IterativeQuickSort {
    swap(arr, i, j) {
        if (i !== j) {
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
    }

    partition(arr, l, h) {
        const pivot = arr[h];
        let boundary = l - 1;
        for (let current = l; current < h; current++) {
            if (arr[current] <= pivot) {
                this.swap(arr, ++boundary, current);
            }
        }
        this.swap(arr, boundary + 1, h);
        return boundary + 1;
    }

    // Store pending ranges in an array instead of using recursive calls.
    QuickSort(arr, l, h) {
        if (l >= h) {
            return;
        }

        const ranges = [[l, h]];
        while (ranges.length > 0) {
            const [low, high] = ranges.pop();
            const pivotIndex = this.partition(arr, low, high);
            if (low < pivotIndex - 1) {
                ranges.push([low, pivotIndex - 1]);
            }
            if (pivotIndex + 1 < high) {
                ranges.push([pivotIndex + 1, high]);
            }
        }
    }

    printArr(arr, n) {
        console.log(arr.slice(0, n).join(" "));
    }
}

const ob = new IterativeQuickSort();
const arr = [4, 3, 5, 2, 1, 3, 2, 3];
ob.QuickSort(arr, 0, arr.length - 1);
ob.printArr(arr, arr.length);
