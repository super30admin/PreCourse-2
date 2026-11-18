// Time: O(n log n); Space: O(n)

class MergeSort {
    // Merge the already sorted ranges arr[l..m] and arr[m+1..r].
    merge(arr, l, m, r) {
        const merged = [];
        let left = l;
        let right = m + 1;

        // Taking from the left on ties keeps the sort stable.
        while (left <= m && right <= r) {
            merged.push(arr[left] <= arr[right] ? arr[left++] : arr[right++]);
        }
        while (left <= m) {
            merged.push(arr[left++]);
        }
        while (right <= r) {
            merged.push(arr[right++]);
        }
        for (let i = 0; i < merged.length; i++) {
            arr[l + i] = merged[i];
        }
    }

    sort(arr, l, r) {
        if (l < r) {
            const middle = l + Math.floor((r - l) / 2);
            this.sort(arr, l, middle);
            this.sort(arr, middle + 1, r);
            this.merge(arr, l, middle, r);
        }
    }

    printArray(arr) {
        console.log(arr.join(" "));
    }
}

const arr = [12, 11, 13, 5, 6, 7];
const ob = new MergeSort();
console.log("Given Array");
ob.printArray(arr);
ob.sort(arr, 0, arr.length - 1);
console.log("\nSorted array");
ob.printArray(arr);
