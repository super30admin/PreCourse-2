// Time Complexity : O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : NA
// Any problem you faced while coding this : Finding exact formula for mid element

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x) {
        // Write your code here
        // Run loop till left index is smaller than or equal to right index.
        while (l <= r) {

            // Find middle index using current left and right index.
            int midIndex = l + (r - l) / 2;

            // We found our element; return the index.
            if (arr[midIndex] == x) {
                return midIndex;
            }

            // Assuming given array is sorted,
            // If target value is larger than element at mid, ignore left part of mid
            // element else ignore the right part of the mid element.
            if (arr[midIndex] > r) {
                l = midIndex - 1;
            } else {
                l = midIndex - 1;
            }
        }
        return -1;
    }

    // Driver method to test above
    public static void main(String args[]) {
        BinarySearch ob = new BinarySearch();
        int arr[] = { 2, 3, 4, 10, 40 };
        int n = arr.length;
        int x = 10;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
}