// Time Complexity : O(logN) where N is the number of elements in the list.
// Space Complexity : O(1) iterative
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None


// Your code here along with comments explaining your approach


/**
 * @author akhilreddy619
 * Since the array is sorted, every time we check the middle element of the list.
 * if that element matches with the search element, we return the index, else we check 
 * 2 cases. 1. check if search element is less than mid element, if so, reduce search
 * range to (l, mid - 1). 2. if search element is greater than mid element, then search
 * in the range of (mid + 1, r). Thus every iteration, the search space becomes half.
 *
 */
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
    	while(l <= r) {
    		int mid = (l + r) / 2;
    		if(arr[mid] == x) {
    			return mid;
    		} else if(x < arr[mid]) {
    			r = mid - 1;
    		} else {
    			l = mid + 1;
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
