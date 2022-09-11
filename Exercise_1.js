// Time Complexity : O(log N); N is the array size
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach
/**
 * @param {number[]} nums
 * @param {number} start
 * @param {number} end
 * @param {number} target
 * @return {number}
 */
var binarySearch = function (nums, start, end, target) {
    let mid;
    while (start <= end) {
        mid = Math.ceil((start + end) / 2);
        // Return index if target was fount
        if (nums[mid] === target)
            return mid;
        // if target is a higher number, search in the second half of the array
        // else search in the 1st half
        if (nums[mid] < target) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    return -1;
};

let arr = [2, 3, 4, 10, 40];
let n = arr.length;
let x = 10;
let result = binarySearch(arr, 0, n - 1, x);
if (result == -1)
    console.log("Element not present");
else
    console.log("Element found at index " + result); 
