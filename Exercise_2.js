class QuickSort {

      /* This function takes last element as pivot,
           places the pivot element at its correct
           position in sorted array, and places all
           smaller (smaller than pivot) to left of
           pivot and all greater elements to right
           of pivot */

    //swap(arr, i, j) {
        //Your code here
    //}

    //partition(arr, low, high) {
        //Write code here for Partition and Swap
    //}

     /* The main function that implements QuickSort()
          arr[] --> Array to be sorted,
          low  --> Starting index,
          high  --> Ending index */
    sort(arr) {
        if(arr.length <= 1)
        {
            return arr;
        }
             // Recursively sort elements before
             // partition and after partition
        let pivot = arr[arr.length-1];
        let left = [];
        let right = [];
        for(let i=0;i<arr.length-1;i++)
        {
            if(arr[i]<=pivot){
                left.push(arr[i]);
            }
            else{
                right.push(arr[i]);
            }

        }
        return[...this.sort(left),pivot,...this.sort(right)];
    }

      /* A utility function to print array of size n */
    printArray(arr) {
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
    arr = ob.sort(arr);
    console.log("sorted array");
    ob.printArray(arr);
