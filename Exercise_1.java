// Time Complexity : O(logn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Not on leetcode
// Any problem you faced while coding this : No

class Exercise_1 {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int left, int right, int target) {
        // Write your code here
        while (left <= right) {
            int middle = (left + right - 1) / 2;
            if (arr[middle] == target) {
                return middle;
            }
            if (arr[middle] > target) {
                right = middle - 1;
                continue;
            }
            if (arr[middle] < target) {
                left = middle + 1;
            }
        }
        return -1;
    }

    // Driver method to test above
    public static void main(String args[]) {
        Exercise_1 ob = new Exercise_1();
        int arr[] = { 2, 3, 4, 10, 40 };
        int n = arr.length;
        int x = -1;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
}
