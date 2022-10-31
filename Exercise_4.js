//Time Complexity: O(nlogn)
//Space Complexity: O(n)
const mergeSort = arr => {
  if (arr.length === 1) {
    return arr;
  } else {
    let middle = arr.length / 2;

    let left = arr.slice(0, middle);
    let right = arr.slice(middle);

    return merge(mergeSort(left), mergeSort(right));
  }
};

const merge = (left, right) => {
  let result = [];
  let left_itr = 0;
  let right_itr = 0;

  while (left_itr < left.length && right_itr < right.length) {
    if (left[left_itr] < right[right_itr]) {
      result.push(left[left_itr]);
      left_itr += 1;
    } else {
      result.push(right[right_itr]);
      right_itr += 1;
    }
  }

  while (left_itr < left.length) {
    result.push(left[left_itr]);
    left_itr += 1;
  }

  while (right_itr < right.length) {
    result.push(right[right_itr]);
    right_itr += 1;
  }
  arr = result;
  return result;
};

//  Code to print the list
const printList = arr => {
  return arr;
};

// driver code to test the above code
let arr = [12, 11, 13, 5, 6, 57];
console.log("Given array is", printList(arr));
mergeSort(arr);
console.log("Sorted array is: ", printList(arr));
