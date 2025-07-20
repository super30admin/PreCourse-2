class MergeSort {
     // Merges two subarrays of arr[].
     // First subarray is arr[l..m]
     // Second subarray is arr[m+1..r]
    merge(arr, l, m, r) {
        //Your code here
        let leftSubArrLen = m - l + 1;
        let rightSubArrLen = r - m;

        let leftSubArr = new Array(leftSubArrLen);
        let rightSubArr = new Array(rightSubArrLen);

        for (let i = 0; i < leftSubArrLen; i++) {
            leftSubArr[i] = arr[l + i];
        }

        for (let j = 0; j < rightSubArrLen; j++) {
            rightSubArr[j] = arr[m + 1 + j];
        }

        let i = 0;
        let j = 0; 
        let k = l; 

        while (i < leftSubArrLen && j < rightSubArrLen) {
            if (leftSubArr[i] <= rightSubArr[j]) {
                arr[k] = leftSubArr[i];
                i++;
            } else {
                arr[k] = rightSubArr[j];
                j++;
            }
            k++;
        }

        while (i < leftSubArrLen) {
            arr[k] = leftSubArr[i];
            i++;
            k++;
        }
        while (j < rightSubArrLen) {
            arr[k] = rightSubArr[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    sort(arr, l, r) {
        //Write your code here
        //Call mergeSort from here
        if(l >= r) return;

        let mid = Math.floor(l + (r-l)/2)

        this.sort(arr, l, mid);
        this.sort(arr, mid + 1, r);
        this.merge(arr, l, mid, r);
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
