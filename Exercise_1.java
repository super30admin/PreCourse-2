// Time Complexity : O(logn)
// Space Complexity :O(1)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : No, Have implemented this before so it was easy

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x) {
        // Using the ittrative approch instead of recursive
        int result = -1;
        if (arr.length == 0) {
            return -1;
        }
        while (l < r) {
            int mid = (l + r) / 2;
            if (arr[mid] == x) {
                result = mid;
                break;
            }
            if (arr[mid] > x) {
                r = mid - 1;
            }
            if (arr[mid] < x) {
                l = mid + 1;
            }
        }
        return result;
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
