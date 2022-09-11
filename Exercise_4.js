// Time Complexity : O(nlogn)
// Space Complexity : O(n) where n is the array length
// Did this code successfully run on Leetcode : Not found on leetcode. Ran successfully loacally
// Any problem you faced while coding this : No, once I looked up how merge sorting works


// Your code here along with comments explaining your approach
// Exercise_4 : Merge Sort

/*
Divide and conquer
Divide the array till only 1 element is left in each array.
Then merge each array
*/

let merge = (a1, a2) => {

    let c = [];
    while (a1.length > 0 && a2.length > 0) {
        if (a1[0] < a2[0]) {
            c.push(a1[0]);
            a1.shift();
        } else {
            c.push(a2[0]);
            a2.shift();
        }
    }
    if (a1.length > 0) {
        c = [...c, ...a1];
    }
    if (a2.length > 0) {
        c = [...c, ...a2];
    }
    return c;
}

let mergeSort = (arr) => {
    // Return array id it contains only 1 element
    if (arr.length === 1)
        return arr;
    let midPoint = Math.floor(arr.length / 2);
    // Divide the array into half
    let leftArr = arr.slice(0, midPoint);
    let rightArr = arr.slice(midPoint);

    leftArr = mergeSort(leftArr);
    rightArr = mergeSort(rightArr);

    // Merge each divided array
    return merge(leftArr, rightArr);
}

var arr = [5, 3, 7, 6, 2, 9];
// var arr = [1,0,5,4];
mergeSort(arr);
console.log(mergeSort(arr));

