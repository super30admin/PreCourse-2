// Time Complexity : O(logN)
// Space Complexity : O(logN)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No



class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
    	if(x<arr[l] || x>arr[r] || l>=r) {
    		return -1;
    	}
    	if(arr[l]==x) {
    		return l;
    	}
    	if(arr[r]==x) {
    		return r;
    	}
    	int mid=(l+r)/2;
    	
    	if(x<arr[mid]) {
    		return binarySearch(arr,l,mid,x);
    	}else {
    		return binarySearch(arr,mid,r,x);
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
