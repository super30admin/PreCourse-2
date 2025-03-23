class MergeSort {
     // Merges two subarrays of arr[].
     // First subarray is arr[l..m]
     // Second subarray is arr[m+1..r]
    merge(arr, l, m, r) {
        //Your code here
        let leftSize = m - l + 1;
        let rightSize = r - m;

        // Create temporary arrays
        let left = new Array(leftSize);
        let right = new Array(rightSize);

        // Copy data to temporary arrays left[] and right[]
        for (let i = 0; i < leftSize; i++) {
            left[i] = arr[l + i];
        }
        for (let j = 0; j < rightSize; j++) {
            right[j] = arr[m + 1 + j];
        }

        // Merge the temporary arrays back into arr[l..r]
        let i = 0, j = 0, k = l;

        while (i < leftSize && j < rightSize) {
            if (left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        // Copy remaining elements of left[], if any
        while (i < leftSize) {
            arr[k] = left[i];
            i++;
            k++;
        }

        // Copy remaining elements of right[], if any
        while (j < rightSize) {
            arr[k] = right[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    sort(arr, l, r) {
        if(l<r)
        {
        //Write your code here
        //Call mergeSort from here
        var mid = Math.floor((l+r)/2);
        this.sort(arr,l,mid);
        this.sort(arr,mid+1,r);
        this.merge(arr,l,mid,r);
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


