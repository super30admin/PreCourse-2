//Time Complexity O(n log n)
//Space Complexity O(n)
//Yes
//No

class MergeSort {
     // Merges two subarrays of arr[].
     // First subarray is arr[l..m]
     // Second subarray is arr[m+1..r]
     merge(arr, l, m, r) {
        //Your code here
         let n1 = m - l + 1; //Sizes of two subarrays 
        let n2 = r - m;

        // Create temporary arrays
        let L = new Array(n1); 
        let R = new Array(n2);

        // Copy data to temporary arrays L[] and R[]
        for (let i = 0; i < n1; i++) {
            L[i] = arr[l + i];
        }
        for (let j = 0; j < n2; j++) {
            R[j] = arr[m + 1 + j];
        }

        // Merge the temporary arrays back into arr[l..r]
        let i = 0; // Initial index of first subarray
        let j = 0; // Initial index of second subarray
        let k = l; // Initial index of merged subarray

        while (i < n1 && j < n2) {  // Compare elements of both subarrays and merge them in sorted order
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        // Copy the remaining elements of L[], if there are any
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        // Copy the remaining elements of R[], if there are any
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }
    // Main function that sorts arr[l..r] using
    // merge()
     sort(arr, l, r) {
        //Write your code here
        //Call mergeSort from here
          if (l < r) {
            // Find the middle point
            let m = Math.floor((l + r) / 2);

            // Recursively sort the first and second halves
            this.sort(arr, l, m);
            this.sort(arr, m + 1, r);

            // Merge the sorted halves
            this.merge(arr, l, m, r);
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
    // Driver method
     let arr = [12, 11, 13, 5, 6, 7];
     console.log("Given Array");
     let ob = new MergeSort();
     ob.printArray(arr);
     ob.sort(arr, 0, arr.length - 1);
     console.log("\nSorted array");
     ob.printArray(arr);


