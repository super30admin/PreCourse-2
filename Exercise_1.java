class BinarySearch { 
    //time compexity o(logn)
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
    	int mid=(l)+(r-l)/2;
    	if(arr[mid]==x)
    		return mid;
    	else if(arr[mid]>x)
    		return binarySearch(arr, l, mid-1, x);
    	else
    		return binarySearch(arr, mid+1, r, x);
    	
        //Write your code here
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 40; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
