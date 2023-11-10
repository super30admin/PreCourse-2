//Precourse 2: Exercise 2    --  Implementing Singly Linked List 
//1441. Build an Array With Stack Operations
// Time Complexity : O(log n) because we divided the array into half and kept searching in it. In short we straight away reducing the half part of array
// Space Complexity : O(n) required for storing n elements
// Any problem you faced while coding this : no

/*Output
Element found at index 3*/


public class binarySearchPC2 {
	    // Returns index of x if it is present in arr[l.. r], else return -1 
	    int binarySearchPC2(int arr[], int l, int r, int x) 
	    {
	        //Write your code here
			//l is the low and r is the high in given array from 0 to n-1
	    	if(r>l) {
	    	int mid= l+((r-l)/2);  // to avoid integer overflow
	    	if(x == arr[mid])
	    		return mid;
	    	
	    	if(x > arr[mid])
	    		return binarySearchPC2(arr, mid+1, r, x);

	    	if(x < arr[mid])
	    		return binarySearchPC2(arr, l, mid-1, x);
	    	}
	    	// We reach here when element is not present
	        // in array
	        return -1;
	    } 
	  
	    // Driver method to test above 
	    public static void main(String args[]) 
	    { 
	    	binarySearchPC2 ob = new binarySearchPC2(); 
	        int arr[] = { 2, 3, 4, 10, 40 }; 
	        int n = arr.length; 
	        int x = 10; 
	        int result = ob.binarySearchPC2(arr, 0, n - 1, x); 
	        if (result == -1) 
	            System.out.println("Element not present"); 
	        else
	            System.out.println("Element found at index " + result); 
	    } 
}
