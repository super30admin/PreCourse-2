package Exercise1;

// Time Complexity : O(log n), where n is the length of the array
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : yes done some questions that use binary search
// Any problem you faced while coding this : No
class BinarySearch {

    int binarySearch(int arr[], int l, int r, int x) 
    {
        while(l <= r) {
            // middle index of the sub array
            int mid = (r - l) / 2 +  l;
            // if mid index is element return index
            if(arr[mid] == x) {
                return mid;
            } else if(arr[mid] < x) {
                l = mid +1;
            } else {
                r = mid -1;
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
