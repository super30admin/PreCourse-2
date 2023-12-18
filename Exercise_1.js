//Time Complexity O(log n)
//Space Complexity O(1)
//Yes
//No

// BinarySearch class to perform binary search on a sorted array
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    binarySearch(arr, l, r, x) {
        // Initialize a variable to store the midpoint
        let midpoint;

        // Perform binary search while the left pointer is less than or equal to the right pointer
        while (l <= r) {
            // Calculate the midpoint of the current range
            midpoint = Math.floor((l + r) / 2);

            // If the element at the midpoint is equal to the target value, return the midpoint
            if (arr[midpoint] === x) {
                return midpoint;
            }
            // If the element at the midpoint is less than the target value, update the left pointer
            else if (arr[midpoint] < x) {
                l = midpoint + 1;
            }
            // If the element at the midpoint is greater than the target value, update the right pointer
            else if (arr[midpoint] > x) {
                r = midpoint - 1;
            }
            else {
                return -1;
            }
        }

        // If the element is not present in the array, return -1
        return -1;
    }
}

// Driver method to test the binarySearch method
const ob = new BinarySearch();
const arr = [2, 3, 4, 10, 40];
const n = arr.length;
const x = 10;
const result = ob.binarySearch(arr, 0, n - 1, x);

// Display the result
if (result === -1)
    console.log("Element not present");
else
    console.log("Element found at index " + result);
