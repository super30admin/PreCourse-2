class IterativeQuickSort {
    swap(arr, i, j) {
        //Try swapping without extra variable
        if(i != j) {
            arr[i] = arr[i] - arr[j];
            arr[j] = arr[i] + arr[j];
            arr[i] = arr[j] - arr[i];
            return;
        }
    }
      /* This function is same in both iterative and
           recursive*/
    partition(arr, low, high) {
        //Compare elements and swap.
        let pivot = arr[high];
        let lp = low - 1;

        for(let j = low; j <= high - 1; j++) {
            if(arr[j] <= pivot) {
                lp++;
                this.swap(arr, lp, j);
            }
        }
        this.swap(arr, lp + 1, high);
        return lp + 1;
    }
     // Sorts arr[l..h] using iterative QuickSort
    QuickSort(arr, l, h) {
        let stack = new Array(h - l + 1);
        let top = -1;

        stack[++top] = l;
        stack[++top] = h;

        while (top >= 0) {
            h = stack[top--];
            l = stack[top--];

            let pivot = this.partition(arr, l, h);

            if ((pivot - 1) > l) {
                stack[++top] = l;
                stack[++top] = pivot - 1;
            }

            if ((pivot + 1) < h) {
                stack[++top] = pivot + 1;
                stack[++top] = h;
            }
        }
    }
     // A utility function to print contents of arr
    printArr(arr, n) {
        let i;
        for (i = 0; i < n; ++i)
            console.log(arr[i] + " ");
    }
}
  // Driver code to test above
let ob = new IterativeQuickSort();
let arr = [4, 3, 5, 2, 1, 3, 2, 3];
ob.QuickSort(arr, 0, arr.length - 1);
ob.printArr(arr, arr.length);
