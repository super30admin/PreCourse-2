//  Python program for implementation of Quicksort

// This function is same in both iterative and recursive
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
const quickSortIterative = arr => {
  let stack = [];
  stack.push(0);
  stack.push(arr.length - 1);

  while (stack[stack.length - 1] >= 0) {
    let h = stack.pop();
    let l = stack.pop();

    let pivot = partition(arr, l, h);

    if (pivot - 1 > l) {
      stack.push(l);
      stack.push(pivot - 1);
    }

    if (pivot + 1 < h) {
      stack.push(pivot + 1);
      stack.push(h);
    }
  }
};

//  Driver code to test above
let arr = [7, 4, 1, 6, 5, 0];
let n = arr.length;
quickSortIterative(arr);
console.log("Sorted array is:");
for (let i in arr) {
  console.log(arr[i]);
}
