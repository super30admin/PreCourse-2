// Time Complexity : O(logn) when the array is sorted
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : did not find on the leetcode
// Any problem you faced while coding this : no


// Your code here along with comments explaining your approach
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
    	int left=l, right=r;
    	 
    	// left pointer is increasing , and right pointer is decreasing. The moment they cross each other means the elemen was not found
    	while (left <=right ) { 
    		// Find the mid of the array
    		int mid = (left+right) == 0 ? 0 : ((left+right)/2); 
    		if(arr[mid] == x) { // Check if the element is present on the mid of the array
    			return mid;
    		}
    		// We did not find the element in the mid, so we know that the array is sorted, as it is a condition of Binary Search
    		
    		if(x < arr[mid]) {
    			// go left, as lesser elements will be on left part of the array
    			right = mid-1;
    		}
    		else {
    			// go right , as the bigger element will be on the right side of the array 
    			left = mid+1;
    		}
    	}
    	// returning -1 if we did not find the element
    	return -1;
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
