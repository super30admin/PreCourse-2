// Time Complexity : O(logn)
// Space Complexity :   O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None 


// Your code here along with comments explaining your approach

class BinarySearch { 
    // Returns index of x if it is present in arr[l..r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) { 
        if (l <= r) {
            int mid = l + (r - l) / 2; // Prevents integer overflow

            // Check if x is at mid
            if (arr[mid] == x)
                return mid;

            // If x is smaller, search the left subarray
            if (arr[mid] > x)
                return binarySearch(arr, l, mid - 1, x);

            // Otherwise, search the right subarray
            return binarySearch(arr, mid + 1, r, x);
        }

        // Element is not present in the array
        return -1;
    } 

    // Driver method to test the above 
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
