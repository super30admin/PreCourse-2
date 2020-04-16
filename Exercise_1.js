// Exercise_1 : Binary Search.

function binarySearch(arr, x) {
    let mid = Math.floor(arr.length / 2);
    let left = 0;
    let right = arr.length - 1;
    while(left <= right) {
        if(arr[mid] === x) {
          console.log('Element found at index ' + mid);
          return;
        }
        else if(x > arr[mid]) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
        mid = Math.floor((right + left) / 2);
    }
    console.log('Element not present');
}


binarySearch([2,3,4,10,40], -9);