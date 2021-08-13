
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
function quickSort(arr, left = 0, right = arr.length - 1) {
    let stack = [];
    stack.push({ l: left, r: right });

    //Iterate the stack 
    //partition the array along the pivot 
    //but retreiving the start and end index from the stack
    while (stack.length) {
        const { l, r } = stack.shift();

        let pivotIndex = pivot(arr, l, r);

        if (pivotIndex - 1 > l) {
            stack.push({ l: l, r: pivotIndex - 1 });
        }

        if (pivotIndex + 1 < r) {
            stack.push({ l: pivotIndex + 1, r: r });
        }
    }
    return arr;
}

quickSort([4, 1, 3, 2, 5, 7, 6, 8]);