//Time Complexity: O(logn)
//Space Complexity: O(1)

//  Javascript code to implement iterative Binary Search.
//  It returns location of x in given array arr
//  if present, else returns -1

const binarySearch = (arr, l, r, x) => {
  //write your code here
  while (l <= r) {
    let mid_index = Math.floor((l + r) / 2);
    if (x === arr[mid_index]) {
      return mid_index;
    } else if (x > arr[mid_index]) {
      l = mid_index + 1;
    } else {
      r = mid_index - 1;
    }
  }
  return -1;
};

//   Test array
let arr = [2, 3, 4, 10, 40, 80];
// let x = 10;
let x = 40;
// Function call
const result = binarySearch(arr, 0, arr.length - 1, x);
if (result != -1) {
  console.log("Element is present at index", result);
} else {
  console.log("Element is not present in array");
}
