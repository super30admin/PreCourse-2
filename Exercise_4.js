class MergeSort {
     // Merges two subarrays of arr[].
     // First subarray is arr[l..m]
     // Second subarray is arr[m+1..r]
    //  time complexity: O(r-l+1)
    //  space complexity: O(r-l+1)
    merge(arr, l, m, r) {
        //Your code here
        let n1 = m - l + 1;
        let n2 = r - m;

        let left = new Array(n1);
        let right = new Array(n2);

        for(let i=0; i<n1; i++){
            left[i] = arr[l + i];
        }
        for(let j=0; j<n2; j++){
            right[j] = arr[m + 1 + j];
        }

        // initial index of first and second subarray
        let i=0, j=0;

        // initial index of erged subarray;
        let k = l;
        while(i< n1 && j<n2){
            if(left[i] <= right[j]){
                arr[k] = left[i];
                i++;
            }else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        // Copy the remaining elements of left[], if there are any
        while (i < n1) {
            arr[k] = left[i];
            i++;
            k++;
        }

        // Copy the remaining elements of right[], if there are any
        while (j < n2) {
            arr[k] = right[j];
            j++;
            k++;
        }

    }
​
    // Main function that sorts arr[l..r] using
    // merge()
    //  time complexity: O(n log n)
    //  space complexity: O(n)
    sort(arr, l, r) {
        //Write your code here
        //Call mergeSort from here
        if (l < r) {
            // Find the middle point
            let m = Math.floor(l + (r - l) / 2);
            // Sort first and second halves
            this.sort(arr, l, m);
            this.sort(arr, m + 1, r);
        
            // Merge the sorted halves
            this.merge(arr, l, m, r);
        }
    }
​
     /* A utility function to print array of size n */
     //  time complexity: O(n)
    //  space complexity: O(1)
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
​
​

