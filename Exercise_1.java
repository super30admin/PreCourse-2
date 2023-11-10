// Time Complexity : O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : No 

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x) {
        // Write your code here
        while (l <= r) {
            int mid = (l + r) / 2;
            if (x == arr[mid]) { // when x is present at mid.
                return mid;
            }
            if (x < arr[mid]) { // when x is present between indices 1 and mid
                r = mid - 1;
            } else {
                l = mid + 1; // when x is present between mid and n
            }
        }
        return 0;

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
