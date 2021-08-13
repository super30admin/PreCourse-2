class BinarySearch { 
   // Time Complexity : O(LogN)
    // Space Complexity : O(1)
    // Did this code successfully run on Leetcode : Yes
    // Any problem you faced while coding this : No
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //using loop to search required number
        if(l>r) {
			return -1;
		}
		int mid = (l+r)/2;
		if(arr[mid]== x) {
			return mid;
		}else if(arr[mid]>x) {
			return binarySearch(arr,l,mid-1,x);			
		}else {
			return binarySearch(arr,mid+1,r,x);
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
