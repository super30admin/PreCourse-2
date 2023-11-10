// Time Complexity : O(1)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x) {
        // Write your code here

        // traverse till left pointer and right pointer is not cross each other
        while (l <= r) {
            // find the middle of the array
            int mid = (l + r) / 2;

            // if middle element is less than our target element than left pointer will be
            // next to mid
            if (arr[mid] < x) {
                l = mid + 1;
            } else if (arr[mid] > x) {
                // else if middle element is greater than our target element than right pointer
                // will be one less than mid
                r = mid - 1;
            } else {
                // if both of condition above mentioned failed means we finf index of target
                // element.
                return mid;
            }

        }
        // if element is not available in the array we return -1;
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
