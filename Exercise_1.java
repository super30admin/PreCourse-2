// Time Complexity : O(log n) → Because with each step, we cut down the search space by half.
// Space Complexity : O(1) → No extra space used apart from a few variables.
// Did this code successfully run on Leetcode: Yes
// Any problem you faced while coding this: No

class BinarySearch { 
    
    /**
     * Binary Search Algorithm
     * 
     * @param arr - The sorted input array
     * @param l - Left boundary of the search space
     * @param r - Right boundary of the search space
     * @param x - Element to search for
     * @return - Index of the element if found, otherwise -1
     */
    int binarySearch(int arr[], int l, int r, int x) { 
        // Continue searching while left index <= right index
        while (l <= r) {
            // ✅ To prevent integer overflow, use this formula
            int mid = l + (r - l) / 2;

            // ✅ Case 1: If middle element is equal to target → return mid
            if (arr[mid] == x) {
                return mid;
            } 
            // ✅ Case 2: If middle element is smaller than target → search right side
            else if (arr[mid] < x) {
                l = mid + 1;
            } 
            // ✅ Case 3: If middle element is greater than target → search left side
            else {
                r = mid - 1;
            }
        }

        // ✅ If element is not present in the array
        return -1;
    } 

    // ✅ Driver method to test the code
    public static void main(String args[]) { 
        BinarySearch ob = new BinarySearch(); 
        
        // ✅ Sample Input and Explanation:
        // Sorted array (binary search only works on sorted arrays)
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 10; // Element to search for

        // ✅ Call binary search
        int result = ob.binarySearch(arr, 0, n - 1, x); 

        // ✅ Output the result
        if (result == -1) {
            System.out.println("Element not present in the array.");
        } else {
            System.out.println("Element found at index " + result);
        }
    } 
}
