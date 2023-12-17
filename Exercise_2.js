class QuickSort {
      /* This function takes last element as pivot,
           places the pivot element at its correct
           position in sorted array, and places all
           smaller (smaller than pivot) to left of
           pivot and all greater elements to right
           of pivot */
     swap(arr, i, j) {
        //Your code here
          let temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
     partition(arr, low, high) {
        //Write code here for Partition and Swap
          let pivot = arr[high];
        let i = low - 1;

        for (let j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                this.swap(arr, i, j);
            }
        }
        this.swap(arr, i + 1, high);
        return i + 1;
    }
     /* The main function that implements QuickSort()
          arr[] --> Array to be sorted,
          low  --> Starting index,
          high  --> Ending index */
     sort(arr, low, high) {
             // Recursively sort elements before
             // partition and after partition
          if (low < high) {
            let index = this.partition(arr, low, high);

            this.sort(arr, low, index - 1);
            this.sort(arr, index + 1, high);
        }
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
    ob.sort(arr, 0, n - 1);
    console.log("sorted array");
    ob.printArray(arr);
