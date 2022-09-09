// Time Complexity : O(nlogn)
// Space Complexity : O(N); where N is the length of array
// Did this code successfully run on Leetcode : Could not find. Ran locally
// Any problem you faced while coding this : Finding the terminating condition


// Your code here along with comments explaining your approach

// Recursive QuickSort
// Logic:
// A pivot value is selected. All values more than that on the left is swapped to right and all values less than it are swapped to left
// The position of pivot is now correct.
// Repeat similar process on th eleft and right sub arrays till the subarray length is 1

var swap = (a, idx1, idx2) => {
    let temp = a[idx1];
    a[idx1] = a[idx2];
    a[idx2] = temp;
}

var partition = (a, left, right) => {
    // Select value at mid point as the pivot
    let pivotVal = a[Math.floor((left + right) / 2)];
    let l = left;
    let r = right;
    while (l <= r) {
        // Find element on the left which is larger than pivot
        while (a[l] < pivotVal) {
            l++;
        }
        // Find element on the right which is smaller than pivot
        while (a[r] > pivotVal) {
            r--;
        }
        if (l <= r) {
            // Swap and move the pointers forward
            swap(a, l, r);
            l++;
            r--;
        }
    }
    return l;
}

var quickSort = (a, left, right) => {
    let index;
    // If single element is left, we do not need to sort it. The array is sorted
    if (items.length > 1) {
        index = partition(a, left, right);
        // There are items on left 
        if (index - 1 > left) {
            quickSort(a, left, index - 1);
        }
        // There are items on the right
        if (index < right) {
            quickSort(a, index, right);
        }
    }
    return a;
}

var items = [5, 3, 7, 6, 2, 9];
console.log(quickSort(items, 0, items.length - 1));


