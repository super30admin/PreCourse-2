class Exercise_1 { 
    // Returns index of x if it is present in arr[l.. r], else return -1
	
	// Time Complexity : O(logn)
	// Space Complexity : O(logn) , worst case - O(n)
	// Did this code successfully run on Leetcode :NA
	// Any problem you faced while coding this : No

	// Your code here along with comments explaining your approach

	
    int binarySearch(int arr[], int l, int r, int x)
    {
    	int low = arr[l];
    	int high = arr[r];
    	int mid = arr[(l+r)/2];
    	
    	if (r >= l && l <=arr.length -1) {
    		if(x == mid)
        		return (l+r)/2;
    		
    		if (low <= x && x < mid) {
        		return binarySearch(arr , l, (l+r)/2 -1, x);
        	}
    		
    		else if (mid < x && x <= high) {
        		return binarySearch(arr , (l+r)/2 +1, r, x);
        	}
    		
    	}
    	return -1;
        
        //Write your code here
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
    	Exercise_1 ob = new Exercise_1();
        //BinarySearch ob = new BinarySearch(); 
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
