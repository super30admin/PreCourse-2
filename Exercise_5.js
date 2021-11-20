// Time Complexity : O(nLogn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : N/a
// Any problem you faced while coding this : Yes. I need to practice quick sort more to obtain a better understanding.

const partition = (arr, start, end) => {
  const pivotValue = arr[end];
  let pIdx = start;
  for (let i = start; i < end; i++) {
    if (arr[i] < pivotValue) {
      [arr[i], arr[pIdx]] = [arr[pIdx], arr[i]];
      pIdx++;
    }
  }

  [arr[pIdx], arr[end]] = [arr[end], arr[pIdx]];
  return pIdx;
};

const iterativeQuickSort = (arr) => {
  stack = [];

  stack.push(0);
  stack.push(arr.length - 1);

  while (stack[stack.length - 1] >= 0) {
    end = stack.pop();
    start = stack.pop();

    pIdx = partition(arr, start, end);

    if (pIdx - 1 > start) {
      stack.push(start);
      stack.push(pIdx - 1);
    }

    if (pIdx + 1 < end) {
      stack.push(pIdx + 1);
      stack.push(end);
    }
  }
  return console.log("array:", arr);
};

iterativeQuickSort([4, 3, 5, 2, 1, 3, 2, 3]);
