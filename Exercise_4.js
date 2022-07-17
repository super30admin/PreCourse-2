function merge(arr, left, mid, right) {
    var x = mid - left + 1;
    var y = right - mid;

    // Create temp arrays
    var leftArr = new Array(x);
    var rightArr = new Array(y);

    // Copy data to temp arrays L[] and R[]
    for (var i = 0; i < x; i++)
        leftArr[i] = arr[left + i];
    for (var j = 0; j < y; j++)
        rightArr[j] = arr[mid + 1 + j];
    var i = 0;
    var j = 0;
    var k = left;

    while (i < x && j < y) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k] = leftArr[i];
            i++;
        } else {
            arr[k] = rightArr[j];
            j++;
        }
        k++;
    }
    while (i < x) {
        arr[k] = leftArr[i];
        i++;
        k++;
    }
    while (j < y) {
        arr[k] = rightArr[j];
        j++;
        k++;
    }
}

function sort(arr, left, right) {
    if (left < right) {
        var mid = left + parseInt((right - left) / 2);
        sort(arr, left, mid);
        sort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    } else return;
}

function printArray(arr) {
    arr.forEach(element => {
        console.log(element);
    })
}

let arr = [12, 11, 13, 5, 6, 7];
console.log("given array is ");
printArray(arr);

sort(arr, 0, arr.length - 1);

console.log('sorted array is');
printArray(arr);

