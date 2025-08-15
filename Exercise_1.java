// Time Complexity : O(log n) — we halve the search range each step
// Space Complexity : O(1) — we use a few variables only
// Any problem you faced while coding this :
//   - Off-by-one mistakes with l, r, and while condition.
//   - Forgetting to move l or r can cause an infinite loop.
//   - Using (l + r) / 2 can overflow for very large indexes; use l + (r - l) / 2 instead.
// Did this code successfully run on Leetcode : Yes
// Your code here along with comments explaining your approach:
//   - Keep two pointers l (left) and r (right).
//   - While l <= r, pick the middle index mid.
//   - If arr[mid] == x → return mid.
//   - If arr[mid] < x → move left bound up: l = mid + 1.
//   - Else move right bound down: r = mid - 1.
//   - If we exit the loop, x is not present → return -1.
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while (l <= r) {
            // Safe mid calculation to avoid potential overflow
            int mid = l + (r - l) / 2;

            if (arr[mid] == x) {
                return mid; // found
            } else if (arr[mid] < x) {
                l = mid + 1; // search right half
            } else {
                r = mid - 1; // search left half
            }
        }
        return -1; // not found
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
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
