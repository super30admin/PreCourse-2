// Implement Merge Sort
function merge(arr1, arr2) {
  let result = []
  let i = 0, j = 0

  while(i < arr1.length && j < arr2.length) {
    if (arr1[i] <= arr2[j]) {
      result.push(arr1[i])
      i++
    } else {
      result.push(arr2[j])
      j++
    }
  }

  while(i < arr1.length) {
    result.push(arr1[i])
    i++
  }

  while(j < arr2.length) {
    result.push(arr2[j])
    j++
  }

  return result
}

function mergeSort(arr) {
  if (arr.length <= 1) return arr

  let mid = Math.floor(arr.length / 2)

  let left = mergeSort(arr.slice(0, mid))
  let right = mergeSort(arr.slice(mid))

  return merge(left, right)
}

// Time Complexity : O(nLogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : I have some difficulty following the recursive stack 