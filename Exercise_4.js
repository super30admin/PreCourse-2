/*
*
* * TC: O(n log n)
* SC: O (n)
* */

class MergeSort {
  // Merges two subarrays of arr[].
  // First subarray is arr[l..m]
  // Second subarray is arr[m+1..r]

  merge(arr, l, m, r) {
    //Your code here
    var temp = []; //create temp array to hold num
    var i, left_end, num_elements, tmp_pos;
    left_end = (m - 1);
    tmp_pos = l;
    num_elements = (r - l + 1);
    while ((l <= left_end) && (m <= r)) {
      if (arr[l] <= arr[m]) // compare l and middle if l is small add left
        temp[tmp_pos++] = arr[l++]; // into the temp array
      else
        temp[tmp_pos++] = arr[m++]; // else place right into the temp array
    }
    while (l <= left_end) // if right is placed in temp arrat then enter the
      temp[tmp_pos++] = arr[l++];// remaining left element
    while (m <= r)// if left element is placed in temp then copy the remaining
      temp[tmp_pos++] = arr[m++];// right element in temp

    for (i = 0; i < num_elements; i++) {//copies temp array back to arr
      arr[r] = temp[r];
      r--;
    }
  }

  // Main function that sorts arr[l..r] using
  // merge()

  sort(arr, l, r) {
    //Write your code here
    //Call mergeSort from here
    var length = arr.length;
    var middle = Math.floor((l + r) / 2);
    if (r > l) {
      this.sort(arr, l, middle);
      this.sort(arr, middle + 1, r);
      this.merge(arr, l, middle + 1, r);

    }
  }

  /* A utility function to print array of size n */

  printArray(arr) {
    let n = arr.length;
    for (let i = 0; i < n; ++i)
      console.log(arr[i] + ' ');
    console.log();
  }
}

// Driver method
let arr = [12, 11, 13, 5, 6, 7];
console.log('Given Array');
let ob = new MergeSort();
ob.printArray(arr);
ob.sort(arr, 0, arr.length - 1);
console.log('\nSorted array');
ob.printArray(arr);
