class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
    	//Termination condition: Once the left exceeds right we need to stop just because the element is not present
    	while(l<=r) {
    		int mid = (l+r)/2;
    		//if found at mid position
    		if(arr[mid] == x)
    			return mid;
    		//if mid is less than the x we increment the left (mid + 1) index keeping right as same else we decrement right by (mid - 1) keeping left same
    		if(arr[mid] < x)
    			l=mid+1;
    		else
    			r=mid-1;
    	}
    	return -1;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 12; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
