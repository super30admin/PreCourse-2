class QuickSort {
​
      /* This function takes last element as pivot,
           places the pivot element at its correct
           position in sorted array, and places all
           smaller (smaller than pivot) to left of
           pivot and all greater elements to right
           of pivot */
​
    function swap(arr, i, j) {
        //Your code here
    }
​
    function partition(arr, low, high) {
        //Write code here for Partition and Swap
    }
​
     /* The main function that implements QuickSort()
          arr[] --> Array to be sorted,
          low  --> Starting index,
          high  --> Ending index */
    function sort(arr, low, high) {
             // Recursively sort elements before
             // partition and after partition
    }
​
      /* A utility function to print array of size n */
    function printArray(arr) {
        let n = arr.length;
        for (let i = 0; i < n; ++i)
            console.log(arr[i] + " ");
        console.log();
    }
}
    // Driver program
    let arr = [10, 7, 8, 9, 1, 5];
    let n = arr.length;
    let ob = new QuickSort();
    ob.sort(arr, 0, n - 1);
    console.log("sorted array");
    ob.printArray(arr);
