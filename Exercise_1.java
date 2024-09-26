// Time Complexity : O(log n) as you search on only one half of the array to get an appropriate match
// Space Complexity : O(1) as only three pointers are needed to an existing array
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class BinarySearch {  
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        
        if(arr.length==0) //Edge case if array is empty
        	return -1;
        
        if(l<=r){ // Corner case- left should be less than or equal to right

        	int mid= l+(r-l)/2; // Avoids buffer overflow

        	if(arr[mid] == x) // Checks if x equals middle element of array and returns the index if true
        		return mid;

        	if(arr[mid]>x)  // Checks if x is smaller than middle element of array so do binary search on left hand side of array as array is sorted
        	    return binarySearch(arr,0,mid-1,x);

        	else
        		return binarySearch(arr,mid+1,arr.length-1,x); // else do binary search on right side as x is greater than middle element
        	}
               return -1; // if no match
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
