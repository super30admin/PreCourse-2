// Time Complexity : O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    // In binary search we divide the array into half repeatedly to search for the
    // target value
    // Works for sorted list only
    int binarySearch(int arr[], int l, int r, int x) {
        // Write your code here
        while (l <= r) {
            int midPosition = (l + r) / 2;
            int mid = arr[midPosition];
            if (x == mid) {
                // If target value is equal to the mid value return index of mid value
                return midPosition;
            } else if (x < mid) {
                // If target value is less than the mid value, search in the left sub array
                r = midPosition - 1;
            } else if (x > mid) {
                // If target value is greater than the mid value, search in the right sub array
                l = midPosition + 1;
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
