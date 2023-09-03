/*
* TC: O(n log n)
* SC: O(n)
* */
class IterativeQuickSort {

  swap(arr, i, j) {
    //Try swapping without extra variable
  }

  /* This function is same in both iterative and
       recursive*/

  partition(arr, l, h) {
    //Compare elements and swap.
    var pivot = arr[h];
    var i = l - 1;
    var temp;
    for (let j = l; j <= h - 1; j++) {
      if (arr[j] <= pivot) {
        i++;
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
      }
    }
    temp = arr[i + 1];
    arr[i + 1] = pivot;
    arr[h] = temp;
    i++;

    return i;
  }

  // Sorts arr[l..h] using iterative QuickSort

  QuickSort(arr, l, h) {
    //Try using Stack Data Structure to remove recursion.
    var stack = [];
    var top = -1;
    stack[++top] = l;
    stack[++top] = h;

    while (top >= 0) {
      //pop h and l
      h = stack[top--];
      l = stack[top--];

      var p = this.partition(arr, l, h);

      // If there are elements on
      // left side of pivot, then
      // push left side to stack
      if (p - 1 > l) {
        stack[++top] = l;
        stack[++top] = p - 1;
      }

      // If there are elements on
      // right side of pivot, then
      // push right side to stack
      if (p + 1 < h) {
        stack[++top] = p + 1;
        stack[++top] = h;
      }
    }
  }

  // A utility function to print contents of arr

  printArr(arr, n) {
    let i;
    for (i = 0; i < n; ++i) console.log(arr[i] + ' ');
  }
}

// Driver code to test above
let ob = new IterativeQuickSort();
let arr = [4, 3, 5, 2, 1, 3, 2, 3];
ob.QuickSort(arr, 0, arr.length - 1);
ob.printArr(arr, arr.length);
