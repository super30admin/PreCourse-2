// Online Javascript Editor for free
// Write, Edit and Run your Javascript code using JS Online Compiler
// time complexity = O(log n)
// space complexity = O(1)
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
   binarySearch(arr, l, r, x) {
       while(l <= r){
           let mid = Math.floor(l + (r - l)/2);
           if(arr[mid] === x) {
               return mid;
           } else {
               if(arr[mid] < x){
                   l = mid + 1;
               } else {
                   r = mid - 1;
               }
           }
       }
       return -1;
   }
}
// Driver method to test above
const ob = new BinarySearch();
const arr = [2, 3, 4, 10, 40];
const n = arr.length;
const x = 10;
const result = ob.binarySearch(arr, 0, n - 1, x);
if (result === -1)
   console.log("Element not present");
else
   console.log("Element found at index " + result);
