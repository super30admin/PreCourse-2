function binarySearch(arr, l, n, x) {
    if (l > n) return -1;
  
    let middleElement = Math.floor((l + n) / 2);
  
    if (arr[middleElement] === x) return middleElement;
    if (arr[middleElement] > x) {
      return binarySearch(arr, l, middleElement - 1, x);
    } else {
      return binarySearch(arr, middleElement + 1, n, x);
    }
  }
  
  let arr = [2, 3, 4, 10, 40];
  let n = arr.length;
  let x = 10;
  let result = binarySearch(arr, 0, n - 1, x);
  if (result === -1) console.log("No such element present");
  else console.log("element present at position" + result);
  
  