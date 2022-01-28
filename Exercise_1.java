    // Time Complexity : O(log n), if element at mid O(1)
    // Space Complexity : O(1)
    // Did this code successfully run on Leetcode : Yes
    // Any problem you faced while coding this : No

    class BinarySearch { 
        // Returns index of x if it is present in arr[l.. r], else return -1 
        int binarySearch(int arr[], int l, int r, int x) 
        { 
            // iterate as long as l is less than r
            while (l <= r) {
                int mid = (l + (r-l)/2); //caluclate new mid on each iteration
                if (arr[mid] == x) { // return if element is present at mid
                    return mid;
                } else if (arr[mid] > x) { // if item at mid is greater than element reduce window set r to mid -1
                    r = mid - 1;
                } else { // if item at mid is greater than element reduce window set l to mid +1
                    l = mid + 1;
                }
            }
            return -1; // return -1 if element not present in array
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
