class IterativeQuickSort {
​
    function swap(arr, i, j) {
​
        //Try swapping without extra variable
​
    }
​
      /* This function is same in both iterative and
           recursive*/
    function partition(arr, l, h) {
​
        //Compare elements and swap.
​
    }
​
     // Sorts arr[l..h] using iterative QuickSort
    function QuickSort(arr, l, h) {
​
        //Try using Stack Data Structure to remove recursion.
​
    }
​
     // A utility function to print contents of arr
    function printArr(arr, n) {
        let i;
        for (i = 0; i < n; ++i)
            console.log(arr[i] + " ");
    }
}
​
  // Driver code to test above
let ob = new IterativeQuickSort();
let arr = [4, 3, 5, 2, 1, 3, 2, 3];
ob.QuickSort(arr, 0, arr.length - 1);
ob.printArr(arr, arr.length);
