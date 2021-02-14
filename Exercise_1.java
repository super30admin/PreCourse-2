class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
    	
    	
        //Write your code here
  //Write your code here
    	
    	
    	while(l<=r)
    	{	//get the mid element
    	    int mid = l+(r-l)/2;
    	    //if at mid   
	    	if(arr[mid]==x)
	    	{
	    		System.out.println("element is"+arr[mid]);
	    		return mid;
	    	}
	    	//right side to mid
	    	if(arr[mid]<x)
	    	{
	    		l=mid+1;
	    		r=arr.length-1;
	    	}	
	    	//left side to mid
	    	else
	    	{
	    		l=0;
	    		r=mid-1;
	    	}
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
