// Time Complexity : O(n)
// Space Complexity :
// Did this code successfully run on Leetcode :Yes 
// Any problem you faced while coding this : Overflow error, found solution on stack overflow.
// Your code here along with comments explaining your approach
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
    	if (r < 1) {
    		return -1;
    	}
    	
        //Write your code here
    	// To avoid overflow
    	int mid = l + (r - l) / 2;
        if (x < arr[mid]) {
            return binarySearch(arr, l, mid - 1, x);
        } else if (x == arr[mid]) {
            return mid;
        } else {
            return binarySearch(arr, mid + 1, r, x);
        }
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
