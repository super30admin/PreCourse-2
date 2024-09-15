class MergeSort {
     // Merges two subarrays of arr[].
     // First subarray is arr[l..m]
     // Second subarray is arr[m+1..r]
    function merge(arr, l, m, r) {
        //Your code here
    }
​
    // Main function that sorts arr[l..r] using
    // merge()
    function sort(arr, l, r) {
        //Write your code here
        //Call mergeSort from here
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
    // Driver method
     let arr = [12, 11, 13, 5, 6, 7];
     console.log("Given Array");
     let ob = new MergeSort();
     ob.printArray(arr);
     ob.sort(arr, 0, arr.length - 1);
     console.log("\nSorted array");
     ob.printArray(arr);
​
​

