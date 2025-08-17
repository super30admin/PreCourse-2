// Time Complexity : O(logn)
// Space Complexity :O(1)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    {
        // While the leftmost point of the array is less than or equal to the rightmost
        while (l <= r) {

            // Finds middle point of array
            int mid = l + (r - l) / 2;

            //If the midpoint is the target, return it
            if (arr[mid] == x) {
                return mid;
            } else {
                // If the target is greater than the midpoint, update the left index to be one ahead of the midpoint
                if (arr[mid] < x) {
                    l = mid + 1;
                    // If the target is less than the midpoint, update the right index to be one less the midpoint
                } else if (arr[mid] > x) {
                    r  = mid - 1;
                }
            }
        }
        return -1;
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
