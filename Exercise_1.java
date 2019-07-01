class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here

    	int indexOfKey = -1;

    	/*  Code not working because i am calling the function recursively but not
    	 *  returning value recursively. only returning
    	 *  when key = arr [mid] and element is not found.
    	 *  so here if they element found also , we are returning the index of key default value. i.e. -1

    	int mid = (l+r)/2;
    	if(l<=r) {
    	if(x == arr[mid])
         	 return mid;   //    	//basecase
    	else if (x <= arr[mid] ) {
    		binarySearch(arr,l,(mid-1),x); // searching  left half of the mid value.
    	}else
    		binarySearch(arr,(mid+1),r,x);  // searching right half of the mid value.
    	}

    	*/

    	// Think of the smaller problems  say n= 1 , i.e array has only one element.

    	if( l == r) {
    		if(arr[l] == x) return l;
    		else return indexOfKey;
    	}else {
    		int mid = (l+r)/2;
    		if(x == arr[mid]) {
    			indexOfKey = mid;
    			return indexOfKey;
    		}else if (x <= arr[mid] ) {
        		return binarySearch(arr,l,(mid-1),x); // searching  left half of the mid value.
        	}else {
        		return binarySearch(arr,(mid+1),r,x);  // searching right half of the mid value.
        	}
    	}
    } 
  
    int binarySearchIterative(int arr[], int l, int r, int x)
    {
        //Write your code here
    	int indexOfKey = -1;
    	int mid=0;
    	while(l<=r) {
    		mid = (l+r)/2;
    		if(x == arr[mid]) {
    			return mid;
    		}
    		else if(x <= arr[mid]) {
    			r = mid -1;
      		}
    		else {
    			l = mid + 1;
    		}
    	}

    	return indexOfKey;
    }


    // Driver method to test above 
    public static void main(String[] args)
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 10; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index :" + result);

        int resultIterative = ob.binarySearchIterative(arr, 0, n - 1, x);
        if (resultIterative == -1)
            System.out.println("Element not present through Iterative process.");
        else
            System.out.println("Element found at index through Iterative process :" + resultIterative);
    } 
}
