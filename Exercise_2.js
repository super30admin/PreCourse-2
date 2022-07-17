function swap(arr, a, b) {
    let temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
  }
  
  function partition(arr, low, high) {
    let pivot = arr[high];
  
    let smallEleIndex = low - 1;
  
    for (let count = low; count <= high - 1; count++) {
      if (arr[count] < pivot) {
        smallEleIndex++;
        swap(arr, smallEleIndex, count);
      }
    }
  
    swap(arr, smallEleIndex + 1, high);
    return smallEleIndex + 1;
  }
  
  function quickSort(arr, low, high) {
    if (low < high) {
      let index = partition(arr, low, high);
      quickSort(arr, low, index - 1);
      quickSort(arr, index + 1, high);
    }
  }
  
  function printArray(arr) {
    arr.forEach(element => {
      console.log(element);
    });
  }
  
  let arr = [10, 7, 8, 9, 1, 5];
  let n = arr.length;
  quickSort(arr, 0, n - 1);
  
  console.log("Sorted Array is");
  printArray(printArray(arr))
  
  