class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
    	//Approach: Array is sorted, and i choose the mid element and compare it with my key
    	//accordingly i will adjust my search and focus on any of the halves of the array
    	while(l <= r)
    	{
    		int mid = (l + r)/2;
    		if(arr[mid] == x)
    			return mid;
    		else if(x < arr[mid])
    			r = mid-1;
    		else
    			l = mid+1;
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
//Time Complexity : O(log n), we apply this binary search in a sorted array and on each loop 
//we divide our search space by half. thats the reason we have O(log n) complexity.
// Space Complexity : O(1) no extra space is used
// Did this code successfully run on Leetcode : NA
// Any problem you faced while coding this : No