// Iterative Quick Sort
function partition(arr, start, end) {
  let pivot = start
  let pivotValue = arr[end]

  for (let i = start; i < end; i++) {
    if (arr[i] < pivotValue) {
      [arr[i], arr[pivot]] = [arr[pivot], arr[i]]
      pivot++
    }
  }

  [arr[pivot], arr[end]] = [arr[end], arr[pivot]]
  return pivot
}

function quickSort(arr) {
  let stack = []
  let start = 0
  let end = arr.length - 1
  stack.push({ start, end })

  while (stack.length > 0) {
    let { start, end } = stack.pop()

    if (start >= end) {
      continue
    }

    let pivotIndex = partition(arr, start, end)
    stack.push({ start, end: pivotIndex - 1 })
    stack.push({ start: pivotIndex + 1, end })
  }

  return arr
}

// Time Complexity : O(n^2)
// Space Complexity : O(logn)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :