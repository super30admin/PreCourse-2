//Time Complexity: O(n logn)
//Space Complexity: O(n)



//function to merge two arrays in a sorted order
//O(n) n comparisons per decomposition
function merge(arr1, arr2) {
    let result = [];
    let i = 0;
    let j = 0;
    /*Loop that compares array values 
    and pushes to the result array with smallest value first*/
    while (i < arr1.length && j < arr2.length) {
        if (arr1[i] < arr2[j]) {
            result.push(arr1[i]);
            i++;
        } else {
            result.push(arr2[j]);
            j++;
        }
    }
    //Pushes remainig values to result array
    //When the array lengths are different in size
    while (i < arr1.length) {
        result.push(arr1[i]);
        i++;
    }

    while (j < arr2.length) {
        result.push(arr2[j]);
        j++;
    }

    return result;

}

//function to decompose the array and recursively perform merge on sub arrays
//O(logn) decompositions
function mergeSort(arr) {
    if (arr.length <= 1) return arr;
    let mid = Math.floor(arr.length / 2);
    let left = mergeSort(arr.slice(0, mid));
    let right = mergeSort(arr.slice(mid));

    return merge(left, right);
}

mergeSort([2, 45, 23, 12, 78, 45]);