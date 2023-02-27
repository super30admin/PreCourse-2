//Time Complexity of Merge Sort is O(nlog(n)). Space complexity is O(n) because of an additional array being used
function mergeSort(arr1, arr2) {
    var merged = [];
    var i = 0,
        j = 0;

    while ((i < arr1.length) && (j < arr2.length)) {
        if (arr1[i] < arr2[j]) {
            merged.push(arr1[i]);
            i++;
        } else {
            merged.push(arr2[j]);
            j++;
        }

    }

    if (i <= (arr1.length - 1)) {
        arr1.splice(0, i)
        merged = merged.concat(arr1);
    } else if (j <= (arr2.length - 1)) {
        arr2.splice(0, j)
        merged = merged.concat(arr2)

    }

    return merged;
}

//Using array helper functions to concentrate more on merge sorting
const leftArray = [2,34,0].sort()
const rightArray = [1,6,4].sort()

const sortedArray = mergeSort(leftArray, rightArray)
console.log(sortedArray)