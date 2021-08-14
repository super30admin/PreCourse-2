
//Time Complexity : O(nlogn)  Sorted List - O(n^2)
//Space Complexity: O(log n)


/*
This function takes first element as the pivot,
returns the correct index of the pivot element by
placing elements smaller than pivot elment to its left
and greater values to its right. 

 */

function pivot(arr, start = 0, end = arr.length - 1) {

    /*
    Swap function used to first swap all the smaller elemenst on one side
    then finally to swap the pivot element to its final position
    */
    //O(n) - n comparisons per decomposition
    function swap(arr, index1, index2) {
        let temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }

    let pivot = arr[start];
    let swapIndex = start;
    for (let i = start + 1; i <= end; i++) {
        if (pivot > arr[i]) {
            swapIndex++;
            swap(arr, swapIndex, i);
        }
    }

    swap(arr, swapIndex, start);

    return swapIndex;
}

//Main Quicksort function 
//O(log n) - decompositions
function quickSort(arr, left = 0, right = arr.length - 1) {
    if (left < right) {
        let pivotIndex = pivot(arr, left, right);
        //left subarray
        quickSort(arr, left, pivotIndex - 1);
        //right subarray
        quickSort(arr, pivotIndex + 1, right);
    }
    return arr;
}

quickSort([4, 1, 3, 2, 5, 7, 6, 8]);