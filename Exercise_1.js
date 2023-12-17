class BinarySearch {
     // Returns index of x if it is present in arr[l.. r], else return -1
     binarySearch(arr, l, r, x) {
         let midpoint 
         while(l<=r){
               midpoint = Math.floor((l+r)/2);
              if(arr[midpoint]===x){
                   return midpoint;
    }
              else if(arr[midpoint]<x){
                   l = midpoint +1
              }
              else if(arr[midpoint]>x){
                   r = midpoint -1
              }
              else{
                   return -1;
              }                    
}
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
