// Time Complexity : Time complexity for binary search would be O(log(n)) where n is the number of elements in the array
// Space Complexity : There is no extra space required so space would be O(1)
// Did this code successfully run on Leetcode :yes
// Any problem you faced while coding this : No problems faced

// Your code here along with comments explaining your approach

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x) {
        // Write your code here

        // Creating a while loop to run till we find the element of if l becomes greater
        // than r
        while (l <= r) {
            int mid = l + (r - l) / 2; // Calculating middle element using l and r. Formula is that way so that it does
                                       // not exceed the integer limit
            if (arr[mid] == x) { // If middle element matches the target, return index of middle element
                return mid;
            } else if (arr[mid] > x) { // If middle element is greater than target, take the subset of array before the
                                       // middle element
                r = mid - 1;
            } else { // If middle element is lesser than target, take the subset of array after the
                     // middle element
                l = mid + 1;
            }
        }
        return -1; // Return -1 if target not present in array
    }

    // Driver method to test above
    public static void main(String args[]) {
        BinarySearch ob = new BinarySearch();
        int arr[] = { 2, 3, 4, 10, 40 };
        int n = arr.length;
        int x = 40;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
}
