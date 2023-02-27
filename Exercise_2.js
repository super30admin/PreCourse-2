//  Implementation of Quicksort Sort 
function quickSort(arr) {
  if (arr.length <= 1) return arr
  
  const pivot = arr[arr.length-1]
  const leftArr = []
  const rightArr = []
  for (let i = 0; i < arr.length-1; i++) {
    if (arr[i] < pivot) {
      leftArr.push(arr[i])
    } else {
      rightArr.push(arr[i])
    }
  }

  return [...quickSort(leftArr), pivot, ...quickSort(rightArr)]
}

// Time Complexity : O(n^2)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :