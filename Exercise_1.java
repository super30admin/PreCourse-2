package precourse2;

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { //comparing the value to be searched with the middle element 
    	int mid= (l+r)/2;
    	if(x<arr[mid])	//element lies in the left subarray
    	{r=mid-1;
    		return binarySearch(arr,l,r,x);
    	}
    		if(x>arr[mid])	// element lies in the right subarray
    		{	l=mid+1;
    			return binarySearch(arr,l,r,x);
    		}
    		if(x==arr[mid])
    		{	return mid;
    
    		}	return -1;
       
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