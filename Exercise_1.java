class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    {
        if (l <= r) { 
            int mid = l + (r - l) / 2; 
  
            // If the element is present at the 
            // middle itself 
            if (arr[mid] == x) 
                return mid; 
  
            
            if (arr[mid] > x) 
                return binarySearch(arr, l, mid - 1, x); 
  

            return binarySearch(arr, mid + 1, r, x); 
        } 

        return -1; 
    } 
    
    //leetcode problem
    int search(int[] nums, int target) {
    	
    	int l = 0;
    	int r = nums.length -1;
    	int mid =0;
    	while(l <= r) {
    		mid = l + (r-l)/2;
    		
    		if(nums[mid] == target) return mid;
    		else if(nums[mid] > target) r = mid -1;
    		else if(nums[mid] < target) l = mid+1;
    		else return -1;
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
