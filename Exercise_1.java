class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
    	//r is the length of array
    	//checking is array is empty, if so return -1 
       if(r>=1)
       {
        //Write your code here
    	int mid= (r+l / 2);
    	
    	//if element is the middle most element
    	if(arr[mid] == x)
    		return mid; 
    	
    	//if element is smaller than middle most element,then search the left part of array
    	
    	if (arr[mid] > x)
    		return binarySearch(arr, l, mid-1, x);
    	
    	//if x is greater than middle most element then search in right sub-array
    	else
    		return binarySearch(arr, mid+1, r, x);
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
