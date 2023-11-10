// Time Complexity : O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode:
// Any problem you faced while coding this: At the time of implementation took help of autocomplete

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x) {
        // Write your code here
        int start = l;
        int end = r;
        int res = x;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            // Checking if mid element is greater than result
            // Then searching element in Left side of array, decreasing end
            if (arr[mid] > res) {
                end = mid - 1;
            } 
            // Checking if mid element is less than result
            // Then searching element in right side of array, increasing start
            else if (arr[mid] < res) {
                start = mid + 1;
            } 
            // If search and end pointing to same element that's our result
            else {
                return mid;
            }
        }
        return -1;
    }

    // Driver method to test above
    public static void main(String args[]) {
        BinarySearch ob = new BinarySearch();
        int arr[] = { -2, 3, 4, 10, 40 };
        int n = arr.length;
        int x = 10;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
}
