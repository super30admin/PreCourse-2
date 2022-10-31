//  program for implementation of Quicksort Sort
//Time : O(nlogn)
//Space: O(n)
const partition = (arr, low, high) => {
  let pivotItem = arr[Math.floor((high + low) / 2)];
  let left = low;
  let right = high;
  while (left <= right) {
    while (arr[left] < pivotItem) {
      left += 1;
    }
    while (arr[right] > pivotItem) {
      right -= 1;
    }
    if (left <= right) {
      //Swap Elements
      temp = arr[left];
      arr[left] = arr[right];
      arr[right] = temp;
      left += 1;
      right -= 1;
    }
  }
  return left;
};

//  Function to do Quick sort
const quickSort = (arr, low, high) => {
  if (arr.length > 1) {
    let i = partition(arr, low, high);
    if (low < i - 1) {
      quickSort(arr, low, high - 1);
    }
    if (i < high) {
      quickSort(arr, i, high);
    }
  }
  return arr;
};

//  Driver code to test above
let arr = [10, 7, 8, 9, 1, 5, 13];
let n = arr.length;
quickSort(arr, 0, n - 1);
console.log("Sorted array is:");
for (let i in arr) {
  console.log(arr[i]);
}
