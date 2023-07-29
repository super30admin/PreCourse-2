// Time Complexity : Finding Middle is of O(log N)
// Space Complexity : O(log N)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x) {
        // Write your code here
        int mid = (l + r) / 2;
        System.out.println(mid);
        if (x == arr[mid]) {
            return mid;
        } else if (x < arr[mid] && l <= r) {
            r = mid - 1;
            return binarySearch(arr, l, r, x);
        } else if (x > arr[mid] && l >= r) {
            l = mid + 1;
            return binarySearch(arr, l, r, x);
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