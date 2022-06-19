// Approach used recursive
// Time Complexity : O(log n)
// Space Complexity : O(log n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : Based on the research I have found that although recursive method is easy the iterative method would be efficient
// since its space complexity is O(1), I would like to know more about space complexity like how would i estimate based on what parameters.

function binarySearchRecursiveStrategy(arr, low, high, key) {
  // checking if high is less than low, else it is invalid and we return -1
  if (high >= low) {
    if (arr[low] === key) return low; // Checking if key is found at low index
    if (arr[high] === key) return high; // Checking if key is found at higher index
    mid = low + high / 2;
    if (arr[mid] === key) return mid; // Checking if key is found at mid level index

    // if key is less than element at mid level then it must be in left part of array
    if (key < arr[mid])
      return binarySearchRecursiveStrategy(arr, low, mid - 1, key);
    // if key is greater than element at mid level then it must be in right part of array
    else return binarySearchRecursiveStrategy(arr, mid + 1, high, key);
  }

  return -1;
}

// Approach used iterative
// Time Complexity : O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : None

function binarySearchIterativeStrategy(arr, key) {
  let low = 0;
  let high = arr.length - 1;
  if (arr[low] === key) return low; // Checking if key is found at low index
  if (arr[high] === key) return high; // Checking if key is found at higher index

  // checking if high is less than low, else it is invalid and we return -1
  while (high >= low) {
    mid = Math.floor(low + high / 2);
    if (arr[mid] === key) return mid; // Checking if key is found at mid level index

    // if key is less than element at mid level then it must be in left part of array
    if (key < arr[mid]) high = mid - 1;
    else low = mid + 1;
  }

  return -1;
}

let arr = [2, 3, 4, 10, 40];
let x = 40;
let n = arr.length;
let result = binarySearchRecursiveStrategy(arr, 0, n - 1, x);
let iterativeResult = binarySearchIterativeStrategy(arr, x);
result == -1
  ? console.log("Element is not present in array")
  : console.log("Element is present at index " + result);
iterativeResult == -1
  ? console.log("iterativeResult:Element is not present in array")
  : console.log(
      "iterativeResult:Element is present at index " + iterativeResult
    );
