class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
    	//Here we give condition that right should be always greater than left pointer
    	if(r>=1) {
    		//Calculating middle index of array
    		int middle = l + (r-l)/2;
    		//Checking if element is present 
            if(x < arr[middle]){
               return binarySearch(arr, l, middle - 1, x);
            }
            else if(x > arr[middle]){
               return binarySearch(arr, middle + 1, r, x);
            }
            else if(arr[middle] == x){
                return middle;
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