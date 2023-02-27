//Time complexity = O(log n), Space complexity = O(n)

class BinarySearch {
    constructor(arr) {
      this.array = arr
    }
    
    findIndex(value) {
      let left = 0;
      let right = this.array.length -1
      
      while (left <= right) {
        let mid = (left + right) / 2
        mid = Math.floor(mid)
        
        if (value === this.array[mid]) return 'Index value is ' + mid //Time complexity here is O(1)
        if (value > this.array[mid] ) { left = mid + 1 }
        if (value < this.array[mid]) { right = mid - 1 }
      }
      return -1
    }
  }
  
  const bs = new BinarySearch([1,2,3,4,5,6,7])
  //Returns an index value for present array value
  console.log(bs.findIndex(6))
  //Returns -1 for not existing array value
  console.log(bs.findIndex(9))