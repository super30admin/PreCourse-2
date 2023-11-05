// time complexity is O(log n) and space is O(log n)
class IterativeQuickSort {
    swap(arr, i, j) {
      // Swap two elements in the array without using an extra variable
      if (i !== j) {
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
      }
    }
  
    partition(arr, l, h) {
      // Choose a pivot element, in this case, we'll use the last element
      let pivot = arr[h];
      let i = l - 1;
  
      for (let j = l; j <= h - 1; j++) {
        if (arr[j] < pivot) {
          i++;
          this.swap(arr, i, j);
        }
      }
  
      this.swap(arr, i + 1, h);
      return i + 1;
    }
  
    QuickSort(arr, l, h) {
      // Create a stack for storing the low and high indices
      let stack = new Array(h - l + 1);
  
      // Initialize top of the stack
      let top = -1;
  
      // Push the initial values of l and h to the stack
      stack[++top] = l;
      stack[++top] = h;
  
      // Keep popping from the stack while it is not empty
      while (top >= 0) {
        // Pop high and low
        h = stack[top--];
        l = stack[top--];
  
        // Set the pivot element at its correct position in the sorted array
        let p = this.partition(arr, l, h);
  
        // If there are elements on the left side of the pivot, push them onto the stack
        if (p - 1 > l) {
          stack[++top] = l;
          stack[++top] = p - 1;
        }
  
        // If there are elements on the right side of the pivot, push them onto the stack
        if (p + 1 < h) {
          stack[++top] = p + 1;
          stack[++top] = h;
        }
      }
    }
  
    printArr(arr, n) {
      for (let i = 0; i < n; i++) {
        console.log(arr[i] + " ");
      }
    }
  }
  
  // Driver code to test the IterativeQuickSort class
  let ob = new IterativeQuickSort();
  let arr = [4, 3, 5, 2, 1, 3, 2, 3];
  ob.QuickSort(arr, 0, arr.length - 1);
  ob.printArr(arr, arr.length);
  