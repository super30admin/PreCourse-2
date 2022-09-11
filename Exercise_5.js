// Time Complexity : O(nlogn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Not found. Ran locally
// Any problem you faced while coding this : How to convert recursive to iterative. Could follow once understood the usage of stack


// Your code here along with comments explaining your approach
// Exercise_5 : Iterative Quick Sort.

let swap = (arr, l, r) => {
    let temp = arr[l];
    arr[l] = arr[r];
    arr[r] = temp;
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

let iterativeQuickSort = (arr, l, h) => {
    let stack = [];
    stack.push(l);
    stack.push(h);
    while (stack.length > 0) {
        let high = stack.pop();
        let low = stack.pop();
        let index = partition(arr, low, high);
        if (index - 1 > low) {
            // There are elements in the left
            stack.push(l);
            stack.push(index - 1);
        }
        if (index + 1 < high) {
            // There are elements in the right
            stack.push(index + 1);
            stack.push(h);
        }
    }
}

// let arr = [5, 7, 7, 8, 8, 10];
// var arr = [5, 3, 7, 6, 2, 9];
var arr = [1, 0, 5, 4];
iterativeQuickSort(arr, 0, arr.length - 1);
console.log("arr:", arr);

