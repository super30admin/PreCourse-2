class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
    	//this method assumes that the array is sorted
    	//find the midpoint of the array
    	int mid=0;
    	if(r>=l) //to ensure that the end index is greater than the start index
    	{
    		mid = l+(r-l)/2;
    	//if the key to be searched is the same as the arr[midpoint]; return the index of the midpoint
    		if(x==arr[mid])
    		{
    			return mid;
    		}
    		else if(x<=arr[mid]) //if key is less than the arr[midpoint], then search for the key in the lower half of the array recursively
    		{
    			return binarySearch(arr, l,mid-1,x);
    		}
    		else if(x>arr[mid]) //key>arr[midpoint], then search for the key in the upper half of the array
    		{
    			return binarySearch(arr,mid+1,r,x);
    		}
    	}	
    	return -1;
    	
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40}; 
        int n = arr.length; 
        int x = 10; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 