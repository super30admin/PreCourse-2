/**
 * Time Complexity : O(log n)
 * Space Complexity: O(1)
 * Did this code successfully run on Leetcode : Yes
 * 
 * Any problem you faced while coding this : Does the input array have duplicates in it?
 */
class BinarySearch {
    /**
     * Returns index of target if it is present in arr[l.. r], else return -1
     *
     * @param arr    sorted array of integers
     * @param left   low
     * @param right  high
     * @param target element to be spotted
     * @return index of target if it's present
     */
    int binarySearch(int[] arr, int left, int right, int target) {
        while (left <= right) {
            int mid = left + (right - left) / 2;    // To prevent int overflow in (left + right) / 2
            if (arr[mid] > target)
                right = mid - 1;
            else if (arr[mid] < target)
                left = mid + 1;
            else
                return mid;
        }
        return -1;
    }

    /**
     * Returns index of target if it is present in arr[l.. r], else return -1
     *
     * @param arr    sorted array of integers
     * @param left   low
     * @param right  high
     * @param target element to be spotted
     * @return index of target if it's present
     */
    int binarySearchRecursive(int[] arr, int left, int right, int target) {
        if (left <= right) {
            int mid = left + (right - left) / 2;    // To prevent int overflow in (left + right) / 2
            if (arr[mid] > target)
                return binarySearchRecursive(arr, left, mid - 1, target);
            if (arr[mid] < target)
                return binarySearchRecursive(arr, mid + 1, right, target);
            else
                return mid;
        }
        return -1;
    }

    // Driver method to test above 
    public static void main(String[] args) {
        BinarySearch ob = new BinarySearch();
        int[] arr = {2, 3, 4, 10, 40};
        int n = arr.length;
        int x = 10;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        // int result = ob.binarySearchRecursive(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " +/**/ result);
    }
} 
