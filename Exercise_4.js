// Time Complexity : O(nLogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : N/a
// Any problem you faced while coding this : Yes, due to recursion.

const merge = (arr1, arr2) => {
  let sortedArr = [];

  while (arr1.length && arr2.length) {
    if (arr1[0] < arr2[0]) sortedArr.push(arr1.shift());
    else sortedArr.push(arr2.shift());
  }
  // performs merge
  return sortedArr.concat(arr1.slice().concat(arr2.slice()));
};

const mergeSort = (arr) => {
  if (arr.length <= 1) return arr;
  let mid = Math.floor(arr.length / 2),
    left = mergeSort(arr.slice(0, mid)),
    right = mergeSort(arr.slice(mid));

  return merge(left, right);
};

console.log("the merged and sorted array:", mergeSort([12, 11, 13, 5, 6, 7]));
