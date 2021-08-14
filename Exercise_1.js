//Time Complexity : O(log n)
//Space Complexity: O(1)

function binarySearch(arr, l, r, x) {
    //Finding the middle value of the array
    let mid = Math.floor((l + r) / 2);

    //Loop through by comparing the x value with the mid index element
    while (arr[mid] !== x && l <= r) {
        //Eliminating left or right part of element next to mid index
        if (x < arr[mid]) {
            r = mid - 1;
        } else {
            l = mid + 1;
        }
        mid = Math.floor((l + r) / 2);
    }

    //Return the index if the elemnt is found  or -1 if it does not exist
    return arr[mid] === x ? mid : -1;

}

let arr = [10, 25, 34, 56, 78];
let x = 56;

binarySearch(arr, 0, arr.length - 1, x);