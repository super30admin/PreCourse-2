//Time - O(logn) 
function binarySearch(arr, val) {
    let start = 0;
    let end = arr.length - 1;
  
    while (start <= end) {
      let mid = Math.floor((start + end) / 2);
  
      if (arr[mid] === val) {
        return mid;
      }
  
      if (val < arr[mid]) {
        end = mid - 1;
      } else {
        start = mid + 1;
      }
    }
    return -1;
  }

//Test array 
let arr = [ 2, 3, 4, 10, 40 ] 
let x = 10
  
//Function call 
let result = binarySearch(arr, x) 
console.log(result)
if (result != -1){ 
    console.log("Element is present at index", result)
}
else{
    console.log("Element is not present in array")
}