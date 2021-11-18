// Time Complexity: O(logN)
// Space Complexity: O(1) - constant time
// Did this code successfully run on Leetcode: N/a
// Any problem you faced while coding this: No.

const binarySearch = (inputArr, target) => {
  let start = 0;
  let end = inputArr.length - 1;
  let mid;

  while (start <= end) {
    mid = Math.floor((end + start) / 2);

    if (inputArr[mid] === target) {
      return console.log("Element found at index:", mid);
    } else if (inputArr[mid] < target) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }

  return console.log("Element not present");
};

binarySearch([2, 3, 4, 10, 40], -1);
