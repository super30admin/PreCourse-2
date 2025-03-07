// Time Complexity : O(log n)
// Space Complexity : O(n)
class BinarySearch {
     // Returns index of x if it is present in arr[l.. r], else return -1
    binarySearch(arr, l, r, x) {

        while (l <= r) {
            // Find the middle element
            let mid = Math.floor((l + r) / 2);
            
            // If the target is found, return the middle index
            if (arr[mid] === x) {
                return mid;
            }
            // If the target is smaller, ignore the right half
            else if (arr[mid] > x) {
                r = mid - 1;
            }
            // If the target is larger, ignore the left half
            else {
                l = mid + 1;
            }
        }
        
        // If the target is not found, return -1
        return -1;
​
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
