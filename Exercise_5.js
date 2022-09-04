function quickSortIterative(arr) {
    stack = [];
    stack.push(0);
    stack.push(arr.length - 1);
    while(stack[stack.length - 1] >= 0){
    	end = stack.pop();
        start = stack.pop();
        let pivotIndex = partition(arr, start, end);
        if (pivotIndex - 1 > start){
        	stack.push(start);
            stack.push(pivotIndex - 1);
		}
        if (pivotIndex + 1 < end){
        	stack.push(pivotIndex + 1);
            stack.push(end);
        }
    }
    return arr;
}
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
let array = [10, 7, 8, 9, 1, 5]
console.log(quickSortIterative(array));