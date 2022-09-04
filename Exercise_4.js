function merge(left, right) {
    let arr = []
    while (left.length && right.length) {
        if (left[0] < right[0]) {
            arr.push(left.shift())  
        } else {
            arr.push(right.shift()) 
        }
    }
    return [ ...arr, ...left, ...right ]
}
function mergeSort(array) {
    const half = array.length / 2
    if(array.length < 2){
      return array 
    }
    const left = array.splice(0, half)
    return merge(mergeSort(left),mergeSort(array))
  }
  let arr = [12, 11, 13, 5, 6, 7] 
  console.log(mergeSort(arr)); 
    
    