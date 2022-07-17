function swap(arr, i, j) {
    let temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }
  
  function partition(arr, l, h) {
    let pivot = arr[h];
    let pIndex = l;
  
    for (let i = 0; i < end; i++) {
      if (arr[i] < pivot) {
        swap(arr, arr[i], arr[pIndex]);
        pIndex++;
      }
    }
  
    swap(arr, arr[pIndex], arr[h]);
    return pIndex;
  }
  
  
  //Using an array as JS Arrays have push and pop actions similar to stack
  function quickSort(arr, l, h) {
    let stack = [];
    stack.push({
      startIndex: l,
      endIndex: h
    });
  
    while (stack.length) {
      //remove top most element of array
      let {
        start,
        end
      } = stack.shift();
      
      let pivotIndex = partition(arr, start, end);
  
      if (pivotIndex - 1 > start) {
        stack.push({
          startIndex: start,
          endIndex: pivotIndex - 1
        })
  
        if (pivotIndex + 1 < end) {
          stack.push({
            startIndex: pivotIndex + 1,
            endIndex: end
          });
        }
      }
    }
  }
  
  function printArray(arr) {
    arr.forEach(element => {
      console.log(element);
    });
  }
  
  let arr = [4, 3, 5, 2, 1, 3, 2, 3];
  quickSort(arr, 0, arr.length - 1);
  printArray(arr);
  
  