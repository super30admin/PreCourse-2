function partition(arr,start,end){
    let pivot = arr[end];
    let pivot_index = start;
    for(let i=start;i<end;i++){
        if(arr[i]<pivot){
            [arr[i], arr[pivot_index]] = [arr[pivot_index], arr[i]]
            pivot_index++;
        }
    }
    [arr[pivot_index], arr[end]] = [arr[end], arr[pivot_index]] 
    return pivot_index;
}

function quickSortRecursive(arr, start, end) {
    if (start >= end) {
        return;
    }
    let index = partition(arr, start, end);
    
    quickSortRecursive(arr, start, index - 1);
    quickSortRecursive(arr, index + 1, end);
}
array = [10, 7, 8, 9, 1, 5]
quickSortRecursive(array, 0, array.length - 1)

console.log(array)