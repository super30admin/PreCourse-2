// Time Complexity : O(nLogn) average - O(n^2) worst case
// Space Complexity : O(1) - constant
// Did this code successfully run on Leetcode : N/a
// Any problem you faced while coding this : Yes, because I have trouble with recursion.

const pivot = (nums, left, right) => {
  let p = right;
  let j = left;
  let i = left - 1;

  while (j <= p) {
    if (nums[j] < nums[p]) {
      i++;
      [nums[i], nums[j]] = [nums[j], nums[i]];
      j++;
    } else {
      j++;
    }
  }
  i++;
  [nums[i], nums[p]] = [nums[p], nums[i]];
  return i;
};

const arrSort = (nums, left = 0, right = nums.length - 1) => {
  if (left < right) {
    let pIdx = pivot(nums, left, right);

    arrSort(nums, left, pIdx - 1);
    arrSort(nums, pIdx + 1, right);
  }
  return console.log("sorted arr:", nums);
};

arrSort([10, 7, 8, 9, 1, 5]);
