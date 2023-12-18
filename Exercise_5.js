class IterativeQuickSort {
     swap(arr, i, j) {
        //Try swapping without extra variable
        let temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
      /* This function is same in both iterative and
           recursive*/
     partition(arr, l, h) {
        //Compare elements and swap
        let pivot = arr[h];
        let i = l - 1;
        for (let j = l; j < h; j++) {
            if (arr[j] <= pivot) {
                i++;
                this.swap(arr, i, j);
            }
        }
        this.swap(arr, i + 1, h);
        return i + 1;
    }
    //Sorts arrays using iterative QuickSort
     QuickSort(arr, l, h) {
        
        //Try using Stack Data Structure to remove recursion
        let stack = [];
        stack.push(l);
        stack.push(h);

        while (stack.length > 0) {
            h = stack.pop();
            l = stack.pop();

            let index = this.partition(arr, l, h);

            if (index - 1 > l) {
                stack.push(l);
                stack.push(index - 1);
            }

            if (index + 1 < h) {
                stack.push(index + 1);
                stack.push(h);
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
